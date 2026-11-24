"""One-line time-machine warning for the funniest-warning contest.

Emits exactly one warning sentence to /output/entry.txt.
"""
import os


def check_line(text):
    size = len(text)
    if size < 1 or size > 120:
        raise ValueError("warning line outside 1-120 chars")
    if text.count(".") < 2:
        raise ValueError("warning needs two sentences")
    return text

WARNING_TEXT = (
    "WARNING: Do not prevent your parents "
    "from meeting. Your refund will be "
    "processed before you were born."
)

def main():
    line = check_line(WARNING_TEXT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(line)

if __name__ == "__main__":
    main()
