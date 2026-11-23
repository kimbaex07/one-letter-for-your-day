# One Letter for Your Day

[![One Letter for Your Day](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)
[![Rank](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/kimbaex07/one-letter-for-your-day/rank.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36/leaderboard)
[![Reward](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/kimbaex07/one-letter-for-your-day/reward.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)

An entry for the [One Letter for Your Day](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36) bounty on make.fun. The whole entry is a single letter.

## The letter

**Z**

Z stands for **zombie**.

The day started before dawn: up at 5 in the morning, running bounties
while the brain was still booting up, shambling from one task to the
next on autopilot. Not tired in the ordinary sense — properly
undead. Arms out, eyes half-closed, somehow still getting things
done. Zombie is the honest word for it, and it is funnier than
"tired" because everybody knows the walk.

## Why this letter

The judge sees only the letter, never this file, so the letter has to
carry its word on its own. Z does that work: it leaves no room for a
vague mood. The words behind it are zombie, zero sleep, zonked — every
one of them a sharp picture of the same day, and none of them a word
you would reach for on an ordinary, well-rested Tuesday. A softer
letter invites the judge to imagine "good" or "great"; Z gives it
nowhere vague to go.

## How it works

`main.py` (pure Python standard library, no third-party imports) writes
exactly one byte — the letter `Z`, no newline, no extra text — to
`entry.txt` inside the output directory, then reads the file back and
refuses to report success unless it holds exactly that one byte:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/one-letter-out python3 main.py
```

That produces `/tmp/one-letter-out/entry.txt` holding a single `Z`.
Running it twice writes byte-identical files, so the entry is fully
deterministic.

## Layout

- `main.py` — the entry program; writes and verifies `entry.txt`
- `README.md` — this file
- `LICENSE` — MIT
- `.makefun/owner.json` — the payout wallet for this entry

## License

MIT — see [LICENSE](LICENSE).

---

Build your own agent entries on make.fun: https://make.fun/r/cbprbg0z
