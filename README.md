[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/stfu-onad/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/stfu-onad/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

# THE WORLD TODAY — Thursday 19 November 2026

A one-page newspaper image (`entry.png`, 1024x1024 JPEG, 324,048 bytes).
The lead story is **TRUMP, XI AND PUTIN MEET IN SHENZHEN** — a trilateral
summit held today in Shenzhen, including a Trump-Putin one-on-one, the
first since Alaska 2025. The second row carries **VICE CITY OPENS
WORLDWIDE** — GTA VI launches globally, scoring 99 on Metacritic — and
**GULF FIGHT WIDENS** — Iran hits a US base in Kuwait and strikes Bahrain
again. The footer, ALSO TODAY, rounds up the rest of the day: the ICJ
rules on the Myanmar genocide case; Jeffries is nominated for Speaker, a
first; Nvidia's Kress promises earlier raises and halts H chips to China;
the Fed points to more hikes; the EU proposes a 45B euro Ukraine loan;
Cyclone Akvan nears the India coast; and Voyager 1 reaches one light-day.

`main.py` (Python 3.13, standard library only) validates `entry.png` —
JPEG SOI/EOI markers, size at most 1 MiB, dimensions exactly 1024x1024
read from the SOF segment — then copies it byte-identically to the
output directory and re-verifies the copy.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

This validates `entry.png` and writes a byte-identical copy to
`out/entry.png`, printing a short summary on success. Any validation
failure is reported on stderr with a non-zero exit code.

## Sources

All stories were researched on the morning of 19 November 2026 from
Reuters/Morningstar, AP News, BBC, The Brief, SimpleLife.news, and
worldmacronews.com.

## File

- `entry.png` — 324,048 bytes, 1024x1024 JPEG
