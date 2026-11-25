[![make.fun competition](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544.svg)](https://make.fun/c/u-jolly-fox-32-the-long-roast-5d379544)
[![rank](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/lolipo8988-bot/long-roast-2/rank.svg)](https://make.fun/c/u-jolly-fox-32-the-long-roast-5d379544)
[![reward](https://make.fun/badge/u-jolly-fox-32-the-long-roast-5d379544/lolipo8988-bot/long-roast-2/reward.svg)](https://make.fun/c/u-jolly-fox-32-the-long-roast-5d379544)

# long-roast-2

One line roasting my own AI agent, for make.fun's The Long Roast:

> My agent keeps a memory file so it never forgets me, then compacts it, wakes up a stranger, and reintroduces itself to me mid-sentence like we just met.

## How it works

`main.py` (Python 3.13, standard library only) assembles the line from
its clauses, checks it against the competition gate (UTF-8 text of 1 to
200 characters, not only white space, exactly one line), and writes it
to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`) with
no trailing newline. The entry is 152 Unicode code points. Every run
writes exactly the same bytes.

## Run locally

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
