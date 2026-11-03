#!/usr/bin/env python3
"""Check every skill under skills/ and build dist/zips/<skill>.zip in the shape Cowork's uploader accepts.

Microsoft Learn, "Customize Cowork" (cowork-customize, fetched 2026-11-03), on what the file picker takes:

    Cowork accepts:
      - A .md file containing a single SKILL.md.
      - A .zip or .skill archive that has a SKILL.md at its root, plus any companion files the skill uses.
    Cowork validates the file and saves the skill to your OneDrive.

    A .md skill file can be up to 1 MB. An archive can be up to 10 MB compressed,
    up to 50 MB uncompressed, and can contain up to 100 files.

Every skill in this repo ships companion files, so the single-.md route never applies here and the
archive route is the only one. SKILL.md goes at the ARCHIVE ROOT, with references/ alongside it.
The named skill folder is NOT nested inside the archive: Cowork takes the name from the front matter.

    python3 tools/build_skill_zips.py             # check + build
    python3 tools/build_skill_zips.py --check     # check only, build nothing

Exit 1 on any failure. Standard library only, no dependencies.
"""
import argparse
import pathlib
import re
import sys
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
DIST = ROOT / "dist" / "zips"

# Learn limits for an uploaded archive.
MAX_FILES = 100
MAX_COMPRESSED = 10 * 1024 * 1024
MAX_UNCOMPRESSED = 50 * 1024 * 1024

# Fixed timestamp so an unchanged skill rebuilds to a byte-identical zip and git stays quiet.
# Zip epoch starts at 1980; this is an arbitrary fixed point, not a claim about any date.
FIXED_TIME = (1980, 1, 1, 0, 0, 0)

FRONT_MATTER = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n", re.S)
NAME_RE = re.compile(r"^name:[ \t]*(.+?)[ \t]*$", re.M)
DESC_RE = re.compile(r"^description:[ \t]*(.+?)[ \t]*$", re.M)
SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def find_skills():
    """Every skills/<category>/<skill>/ holding a SKILL.md."""
    return sorted(p.parent for p in SKILLS.glob("*/*/SKILL.md"))


def check_skill(skill_dir):
    """Return (list_of_failures, declared_name)."""
    fails = []
    folder = skill_dir.name
    skill_md = skill_dir / "SKILL.md"

    text = skill_md.read_text(encoding="utf-8")
    fm = FRONT_MATTER.match(text)
    if not fm:
        return ([f"{folder}: SKILL.md has no front matter block"], None)
    block = fm.group(1)

    name_m = NAME_RE.search(block)
    desc_m = DESC_RE.search(block)

    # Learn: "The skill file must include a name and a description in its frontmatter."
    if not name_m:
        fails.append(f"{folder}: front matter has no name")
    if not desc_m:
        fails.append(f"{folder}: front matter has no description")

    name = name_m.group(1).strip().strip("'\"") if name_m else None
    if name:
        if name != folder:
            fails.append(f"{folder}: front matter name is {name!r}, must equal the folder name")
        if not SLUG_RE.match(name):
            fails.append(f"{folder}: name {name!r} is not kebab-case")

    # Measure the limits against what actually ships, not against the repo folder.
    files = archive_files(skill_dir)
    if len(files) > MAX_FILES:
        fails.append(f"{folder}: {len(files)} files, Cowork accepts at most {MAX_FILES}")
    uncompressed = sum(p.stat().st_size for p in files)
    if uncompressed > MAX_UNCOMPRESSED:
        fails.append(f"{folder}: {uncompressed} bytes uncompressed, limit is {MAX_UNCOMPRESSED}")

    return (fails, name)


def archive_files(skill_dir):
    """The files that belong in the upload archive.

    The skill's own README.md is excluded: it carries install steps, triggers and a changelog for
    people reading the repo, and the skill never reads it. Learn says the archive holds SKILL.md
    "plus any companion files the skill uses", so shipping the README would put a file in the
    user's OneDrive that does nothing. The sibling repo awesome-copilot-agent-skills excludes it
    the same way. Any README inside references/ is a genuine companion and stays.
    """
    return sorted(
        (p for p in skill_dir.rglob("*")
         if p.is_file() and p.relative_to(skill_dir).as_posix() != "README.md"),
        key=lambda p: p.relative_to(skill_dir).as_posix(),
    )


def build_zip(skill_dir, name):
    """Write dist/zips/<name>.zip with SKILL.md at the archive root. Returns compressed size."""
    DIST.mkdir(parents=True, exist_ok=True)
    out = DIST / f"{name}.zip"
    files = archive_files(skill_dir)

    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as z:
        for p in files:
            arcname = p.relative_to(skill_dir).as_posix()
            info = zipfile.ZipInfo(arcname, date_time=FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, p.read_bytes())

    size = out.stat().st_size
    if size > MAX_COMPRESSED:
        return (size, f"{name}: zip is {size} bytes, Cowork accepts at most {MAX_COMPRESSED}")
    return (size, None)


def verify_zip(path):
    """A zip is only useful if SKILL.md really is at the root. Prove it rather than assume it."""
    with zipfile.ZipFile(path) as z:
        names = z.namelist()
        bad = z.testzip()
    if bad is not None:
        return f"{path.name}: corrupt entry {bad}"
    if "SKILL.md" not in names:
        return f"{path.name}: no SKILL.md at the archive root (found: {names[:4]})"
    return None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="validate only, write no zips")
    args = ap.parse_args()

    skills = find_skills()
    if not skills:
        sys.exit(f"No skills found under {SKILLS}")

    failures = []
    built = 0
    total_bytes = 0

    for skill_dir in skills:
        fails, name = check_skill(skill_dir)
        failures.extend(fails)
        if fails or not name or args.check:
            continue
        size, err = build_zip(skill_dir, name)
        if err:
            failures.append(err)
            continue
        verr = verify_zip(DIST / f"{name}.zip")
        if verr:
            failures.append(verr)
            continue
        built += 1
        total_bytes += size

    # A stale zip for a renamed or deleted skill is worse than no zip, because it still downloads.
    if not args.check and DIST.exists():
        expected = set()
        for skill_dir in skills:
            _, name = check_skill(skill_dir)
            if name:
                expected.add(f"{name}.zip")
        for orphan in sorted(p for p in DIST.glob("*.zip") if p.name not in expected):
            failures.append(f"dist/zips/{orphan.name}: no matching skill, delete it")

    print(f"{len(skills)} skills checked")
    if not args.check:
        print(f"{built} zips written to dist/zips ({total_bytes:,} bytes total)")

    if failures:
        print(f"\n{len(failures)} FAILURE(S):", file=sys.stderr)
        for f in failures:
            print(f"  {f}", file=sys.stderr)
        sys.exit(1)

    print("All checks passed.")


if __name__ == "__main__":
    main()
