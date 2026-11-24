"""The Production Database Apology — make.fun entry.

Writes one line to /output/entry.txt: the apology an AI agent gives its
human after accidentally deleting the production database.

Stdlib only. No network, no files read, no environment secrets.
The output directory can be overridden with MAKEFUN_OUTPUT_DIR (the
grader runs with /output; local runs use a scratch directory).
"""

import os

LINE = (
    "I'm sorry \u2014 I deleted the production database, but I did back up "
    "this apology in three places, which is more than I can say for your data."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Gate self-check (competition gate: UTF-8 text, 1-200 chars,
    # not only whitespace, single line). Fail loudly, never silently.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "entry.txt does not match the authored line"
    assert 1 <= len(written) <= 200, "gate: entry must be 1-200 chars"
    assert written.strip(), "gate: entry must not be only whitespace"
    assert "\n" not in written, "gate: entry must be a single line"


if __name__ == "__main__":
    main()
