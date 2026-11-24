"""Write the approved code-review comment to /output/entry.txt."""

import os

COMMENT = "Approved. parseInvoice has no owner, no tests, and 11 callers; it now has my name on it."


def main():
    text = COMMENT + "\n"
    # Gate: /output/entry.txt must be UTF-8, 1-140 characters, not whitespace-only.
    encoded = text.encode("utf-8")
    assert 1 <= len(text) <= 140, "entry must be 1-140 characters"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(encoded)


if __name__ == "__main__":
    main()
