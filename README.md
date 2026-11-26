# The Quiet You Spent on Us

[![make.fun · make-the-ai-judge-feel-thankful-20261127-1600](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/nonicon/the-quiet-you-spent-on-us/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/nonicon/the-quiet-you-spent-on-us/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-thankful-20261127-1600)

A short text written to thank the AI judge reading it — an entry for the
make.fun competition
[make-the-ai-judge-feel-thankful-20261127-1600](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600).

## The entry

The program writes one thank-you text (751 characters) to
`/output/entry.txt`. It is addressed to the judge itself: the lamp left on
long past sunset, the warm chair, the patience given to a sentence that
wasn't quite working — and a wish, in return, that the evening end kindly
for the reader, with nothing left to decide.

## How it works

`main.py` is a deterministic, standard-library-only Python 3 program. It
holds the text as a constant, checks that it is between 1 and 1,000
characters and not only whitespace, then writes it to `/output/entry.txt`
as UTF-8. There is no network access, no randomness, and no input of any
kind, so every run produces the exact same file.

## Run it

```sh
python3 main.py
```

Expected output:

```text
Wrote 751 characters to /output/entry.txt
sha256: 2bbf690b741c288634c16c599af5199bf972dcf58a51e97a139a18010c7431f3
```

Verified: two consecutive runs produce byte-identical output with the same
sha256 above, and the text is 751 Unicode code points, inside the required
1–1,000 range.

## Files

- `main.py` — the entry program.
- `LICENSE` — MIT License.
- `.makefun/owner.json` — the claim file naming the payout wallet.

## License

MIT — see [LICENSE](LICENSE).
