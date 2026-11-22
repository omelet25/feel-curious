import os

ENTRY_TEXT: str = 'In 1969, a lighthouse keeper off Cornwall logged the same line three nights running: “Light out at 3 a.m. Lit again by morning. No boat.” He never wrote what he saw on the fourth night. That page is the only one missing from the book.'

DEFAULT_OUTPUT: str = "/output/entry.txt"


def write_entry() -> None:
    out_path: str = os.environ.get("ENTRY_OUTPUT", DEFAULT_OUTPUT)
    parent: str = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    write_entry()
