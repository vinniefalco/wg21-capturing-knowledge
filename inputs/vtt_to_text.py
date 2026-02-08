"""Convert VTT subtitle files to clean plaintext transcripts."""
import re
import sys
from pathlib import Path

VTT_BASE = Path(r"c:/Users/Vinnie/src/stl-video-transcripts/transcripts")

# Prefer edited.vtt over original.vtt
FILES = [
    "2021/2021-09-09/edited.vtt",
    "2022/2022-01-13/original.vtt",
    "2022/2022-04-28/original.vtt",
    "2022/2022-05-12/original.vtt",
    "2022/2022-05-26/edited.vtt",
    "2022/2022-06-09/edited.vtt",
    "2022/2022-06-23/original.vtt",
    "2022/2022-07-07/original.vtt",
    "2022/2022-07-14/original.vtt",
    "2022/2022-08-04/original.vtt",
    "2022/2022-08-25/edited.vtt",
    "2022/2022-09-15/original.vtt",
    "2022/2022-10-13/edited.vtt",
    "2022/2022-11-03/edited.vtt",
    "2022/2022-12-08/original.vtt",
    "2023/2023-01-12/original.vtt",
    "2023/2023-02-07/original.vtt",
    "2023/2023-02-23/original.vtt",
    "2023/2023-03-16/original.vtt",
]

TIMESTAMP_RE = re.compile(r"^\d{2}:\d{2}:\d{2}\.\d{3}\s*-->")
CUE_ID_RE = re.compile(r"^\d+$")

def parse_vtt(path: Path) -> str:
    lines = path.read_text(encoding="utf-8").splitlines()
    text_lines = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line == "WEBVTT":
            continue
        if line.startswith("NOTE "):
            continue
        if TIMESTAMP_RE.match(line):
            continue
        if CUE_ID_RE.match(line):
            continue
        if line == "[silence]":
            continue
        # Decode HTML entities
        line = line.replace("&gt;", ">").replace("&lt;", "<").replace("&amp;", "&")
        text_lines.append(line)

    # Merge consecutive lines into paragraphs.
    # Speaker changes (>> Name:) start new paragraphs.
    paragraphs = []
    current = []
    for line in text_lines:
        if line.startswith(">>") and current:
            paragraphs.append(" ".join(current))
            current = [line]
        else:
            current.append(line)
    if current:
        paragraphs.append(" ".join(current))

    return "\n\n".join(paragraphs)


def main():
    out_dir = Path(r"c:/Users/Vinnie/src/wg21-capturing-knowledge/inputs/stl")
    out_dir.mkdir(exist_ok=True)

    for rel in FILES:
        src = VTT_BASE / rel
        date = rel.split("/")[1]  # e.g. "2021-09-09"
        dest = out_dir / f"{date}.md"
        print(f"Converting {src.name} -> {dest.name} ...", end=" ")
        text = parse_vtt(src)
        dest.write_text(text, encoding="utf-8")
        print(f"{len(text)} chars")

    print(f"\nDone. {len(FILES)} files written to {out_dir}")


if __name__ == "__main__":
    main()
