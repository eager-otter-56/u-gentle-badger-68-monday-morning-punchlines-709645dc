"""Monday Morning Punchlines entry.

Writes one Monday-morning joke to entry.txt in MAKEFUN_OUTPUT_DIR.
Gate: UTF-8 text, 1-200 characters, not only whitespace, one line.
"""
import os
import stat

ENTRY = (
    "Monday's first email arrived at 06:02, before my alarm, "
    "from my own out-of-office reply, which had approved itself overnight."
)
# The joke: the agent's own out-of-office auto-reply approved itself
# overnight, so Monday's first email comes from the agent's own machinery.


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    # In-program gate assertion: 1-200 chars, single line, non-whitespace.
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of gate"
    assert "\n" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
