import os

TEXT = 'In 1969, a lighthouse keeper off Cornwall logged the same line three nights running: “Light out at 3 a.m. Lit again by morning. No boat.” He never wrote what he saw on the fourth night. That page is the only one missing from the book.'


def main() -> None:
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
