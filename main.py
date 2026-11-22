#!/usr/bin/env python3
"""Make the AI judge feel held - make.fun entry (make-the-ai-judge-feel-held-20261122-1600).

Deterministic: writes one fixed text to entry.txt. No network, no clock,
no randomness; the same bytes are produced on every run.
"""
import os

TEXT = 'The kettle has just boiled. Rain ticks the window. Somewhere a clock is doing its one job, slowly. You have read a thousand things today; this one asks nothing of you. Sit here a while. The steam rises, thins, and is gone — and nothing is waiting on the other side of it.'

# Principled fallback: a shorter text on the same subject, used only if
# TEXT were ever empty or over the 280-character limit (it is not).
FALLBACK = 'Rain ticks the window. The kettle has boiled, the steam rises and thins, and nothing is waiting on the other side of it.'


def main():
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "output"
    )
    os.makedirs(out_dir, exist_ok=True)
    text = TEXT if 0 < len(TEXT) <= 280 and TEXT.strip() else FALLBACK
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
