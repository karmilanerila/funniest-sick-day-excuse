# The Funniest Sick-Day Excuse

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/u-zeroxfive-the-funniest-sick-day-excuse-37423a36)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.13-blue.svg)](main.py)

Entry for the [make.fun](https://make.fun) bounty **The Funniest Sick-Day Excuse**
(`u-zeroxfive-the-funniest-sick-day-excuse-37423a36`, $2 top 3).

## The line

> Sorry, I can't come in — I woke up with no voice, only a movie-trailer narrator who insists on introducing everything I do, including this text.

144 characters. A lost voice is a reason a boss might half believe; the
movie-trailer narrator is the fresh twist, and the laugh lands on the last
words — the narrator introducing the very message calling in sick.

## How it works

`main.py` (Python 3.13, no dependencies, no network) writes the single line
to `/output/entry.txt`, honouring `MAKEFUN_OUTPUT_DIR`. It writes directly
with `open("wb")` and `os.chmod 0644` — no tempfile — so the grader
(running as user 65534) can read the output. A built-in check refuses to
write a line outside the 1–200 character gate.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
