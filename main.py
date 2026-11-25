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
    # Pre-write guard: the excuse must be a single line of 1-200 characters.
    if not (1 <= len(LINE) <= 200) or "\n" in LINE or "\r" in LINE:
        raise ValueError("excuse line must be a single line of 1-200 characters")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

    # Read-back round-trip verification: the written file must decode as
    # UTF-8 and match the guarded line exactly.
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != LINE + "\n":
            raise ValueError("entry.txt failed read-back verification")


if __name__ == "__main__":
    main()
