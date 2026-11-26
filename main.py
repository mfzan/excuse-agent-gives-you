"""Entry for make.fun's "The Excuse Your Agent Gives You" bounty.

The program writes exactly one line to /output/entry.txt: the excuse
an AI agent hands its human after shipping a bug. The joke turns on a
delegation loop -- the agent outsourced the fix to a second agent, which
outsourced it straight back, so both agents are now blocked waiting on
each other while the bug ships anyway. No setup paragraph, no second
line: the whole entry is the single line below.

The program is deterministic and needs no network: it writes the same
bytes on every run and exits 0. The output file is left world-readable
(mode 0644) so the grader, which collects outputs as another user, can
read it. Only the file itself is chmodded -- never the /output
directory, which the sandbox owns.
"""

import os

# The entry: one line, 149 characters, under the 200-character limit.
ENTRY = (
    "I outsourced the fix to another agent, who outsourced it straight "
    "back to me, so we're both blocked waiting on each other while the "
    "bug ships anyway."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    # The grader provides /output; create it only if it is missing.
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Write the single line with a trailing newline, as UTF-8.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")
    # World-readable so the grader (uid 65534) can collect it.
    os.chmod(OUTPUT_PATH, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
