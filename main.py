#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters — make.fun entry.

Writes exactly one Wi-Fi network name (exactly 32 characters) to
entry.txt in the output directory.

The name is a fixed, hand-written string: deterministic by construction,
no randomness, no network, no input read. The program resolves the output
directory (ENTRY_OUTPUT_DIR, else /output), creates it, writes the name
with no trailing newline — the gate counts the file at 1 to 32 characters —
and echoes it to stdout so a local run shows what was written.
"""

import os

STORY = "The dog ate my homework. And Dad"

# The gate counts the whole file: 1 to 32 characters. A trailing newline
# would make 33, so the file is written with no newline at all, and the
# length is asserted here so any rewording that breaks the count fails
# loudly at build time instead of silently at the gate.
assert len(STORY) == 32, f"story must be exactly 32 characters, got {len(STORY)}"


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(STORY)
    print(STORY)


if __name__ == "__main__":
    main()
