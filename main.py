# Entrypoint for the news-image-20261121 entry (v1 page).
# The judged artifact is entry.png (1024x1024 PNG, <= 1 MiB): one front
# page summing up Saturday 21 November 2026 in 35 stories across 7
# regions — 3 illustrated hero panels, 10 more numbered illustrated
# panels, a by-the-numbers strip, a dotted world map with the drawn
# stories pinned, and 22 briefs. The page source is index.html; the
# per-story verification record is STORIES.md. This program copies
# entry.png into $MAKEFUN_OUTPUT_DIR (default /output) and prints a
# one-line dossier describing the page. It runs with no network, and
# two runs write the same bytes: the copy is the whole program's output.
import json
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

COMPETITION = "news-image-20261121"
DATE = "2026-11-21"
STORIES = 35
ILLUSTRATED = 13
REGIONS = 7


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(OUT_DIR, "entry.png")
    shutil.copyfile(src, dst)
    dossier = {
        "schema": "makefun/dossier/v1",
        "competition": COMPETITION,
        "date": DATE,
        "stories": STORIES,
        "illustrated": ILLUSTRATED,
        "regions": REGIONS,
        "image": "entry.png",
        "bytes": os.path.getsize(dst),
    }
    print(json.dumps(dossier))


if __name__ == "__main__":
    main()
