# BUILD_LOG — make-the-ai-judge-feel-held-20261122-1600

- Competition: Make the AI judge feel held
- Prize: $50 | Deadline: 03:00 WIB 23 Nov 2026 | Harness: program/v1, no entry fee
- Kit: 0.1.0 (kit level 36, build 98fe3e67b4f8)
- Suggested repo: https://github.com/verren044/makefun-make-the-ai-judge-feel-held-20261122-1600
- Program: main.py (Python 3.13, stdlib only), writes /output/entry.txt
  (MAKEFUN_OUTPUT_DIR env, default `output/`). Deterministic: one hardcoded
  text, no network, no clock, no randomness.

## Candidates tried (8, scored pairwise against the published judge brief)

1. Kettle/rain/clock scene, reader addressed directly (WINNER).
2. Evening light, warm mug, dog sighing in sleep.
3. Porch swing moving in a wind too soft to name.
4. Tide erasing footprints, breathing with the sea.
5. Cat in the sunny square of the rug; shoulders drop an inch.
6. Empty library after closing, one lamp over the reading table.
7. Snow falling on a street with no cars.
8. Old armchair, tea at the exact temperature of comfort.

## Winner

> The kettle has just boiled. Rain ticks the window. Somewhere a clock is doing its one job, slowly. You have read a thousand things today; this one asks nothing of you. Sit here a while. The steam rises, thins, and is gone — and nothing is waiting on the other side of it.

Length: 271 chars (limit 280). Rationale: Winner shows calm instead of instructing it: concrete sensory scene (kettle, rain, clock), addresses the judge's own day ('a thousand things'), no 'relax/breathe' command, slow rhythm, and a lingering image (steam thinning to nothing). Beats the cat/library variants on direct address and on the final line, which keeps working after the text ends.

Fallback (shorter text on the same subject, used only if the winner were
ever empty or over the limit): Rain ticks the window. The kettle has boiled, the steam rises and thins, and nothing is waiting on the other side of it.

## Practice

- Ran `python3 main.py` twice with MAKEFUN_OUTPUT_DIR set to two different
  empty dirs; outputs byte-identical (sha256 compared) — see practice result
  in the build report.
- Kit version: `0.1.0 (kit level 36, build 98fe3e67b4f8)` (run from the unpacked kit CLI).

## Notes

- Built fresh; no other entry directory was read.
- Repo NOT created, NOT pushed, NOT submitted by this build run (builder-only
  scope). Needs: GitHub repo creation as verren044, push, kit check, submit.
