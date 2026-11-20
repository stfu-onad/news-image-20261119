[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/stfu-onad/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/stfu-onad/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

# THE WORLD TODAY — Thursday 19 November 2026 · Final Edition

A one-page newspaper image (`entry.png`, 1024x1024 JPEG, 355,937 bytes),
revised after the day's news was complete (v2; v1 was submitted the same
morning). Five stories, each verified against reporting of 19 November
2026:

- **Lead — TRUMP, XI AND PUTIN SIGN 'DECLARATION TOWARDS PEACE':** the
  trilateral summit in Shenzhen ends with a four-point pact on UN reform,
  oil output, ICC limits and nuclear risk; no deal on Ukraine or Gaza.
- **ANTHROPIC DEBUTS ON NASDAQ:** ANT opens at $111.50, up 34% on the
  $83 IPO price, after a record $81.3B raise valuing the Claude maker at
  about $1.5 trillion.
- **GULF WAR WIDENS:** Iran hits US bases in Kuwait and Bahrain, tankers
  are struck off Oman, and USS Theodore Roosevelt joins two carriers
  already in theatre.
- **COP31 DRAFT DROPS FOSSIL FUELS:** the Antalya text omits the
  fossil-fuel phaseout as talks run into their final night.
- **EISENKOT MOVES TO OUST NETANYAHU:** his bloc vows an emergency
  government while Netanyahu's unity-government offer is called a
  "bluff".

The footer, ALSO TODAY, rounds up the rest of the day: GTA VI launches
worldwide (99 on Metacritic); the ICJ rules on the Myanmar genocide case;
Jeffries is nominated for Speaker, a first; Nvidia's Kress promises
earlier raises and halts H chips to China; the Fed points to more hikes;
the EU proposes a 45B euro Ukraine loan; Cyclone Akvan nears India; and
Voyager 1 reaches one light-day.

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

All stories were verified on 19–20 November 2026 against The Times,
Reuters, Al Jazeera, UN News, BusinessWorld/Reuters, The Motley Fool and
other reporting of the day. Panel photos are AI-rendered illustrations
(no text inside them); all headlines and labels are drawn with PIL, so
every letter is crisp.

## File

- `entry.png` — 355,937 bytes, 1024x1024 JPEG, sha256
  `76510899ad9e9e258291c7ed0d7d1a7ca3c2ac7701aa07551057cfe04895b9f7`
