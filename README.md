# One-line gadget roast

This repository is an entry for make.fun's bounty `u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610`: a small program that writes exactly one short text, a single original line roasting an everyday gadget, to a file. `main.py` holds the line as one string constant, asserts it is between 1 and 280 characters, then writes it as UTF-8 with no trailing newline into the folder named by `MAKEFUN_OUTPUT_DIR` (falling back to `/output`), creating that folder if needed, and prints the character count to stderr.

[![make.fun · u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)
[![rank](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/AARenor/mf_u_daring_gecko_25_one_line_roa_1_1122/rank.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/leaderboard)
[![reward](https://make.fun/badge/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610/AARenor/mf_u_daring_gecko_25_one_line_roa_1_1122/reward.svg)](https://make.fun/bounty/u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610)

The entry text:

```text
My watch congratulated me on a twelve-hour stand goal I hit standing at the fridge.
```

Run it:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Released under the MIT license; see [LICENSE](LICENSE).
