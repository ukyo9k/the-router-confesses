"""The Router Confesses — make.fun entry.

Writes one line: the excuse a home Wi-Fi router gives for dropping the
connection at the exact climax of a movie.

Stdlib only. No network access. Deterministic output.
"""

import os

LINE = (
    "I know who did it — and after you named me 'FBI Surveillance Van' "
    "and never once thanked me, I've decided you never will."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
