# Ghost Karts 🏮

A tiny night-lantern kart loop made for **GitHub Game Off 2026** (theme: **SHIFT**).

- **Arrow keys** to drive, hold **Shift** for gear 2.
- Your best lap is saved as a glowing **ghost** per kin (in your browser's localStorage) — pick whose ghost to race.
- All art is drawn in code; no external assets.

Play: https://multidimensionaldevilskingdomsroute666.github.io/ghost-karts/

`test.py` is an optional headless Playwright smoke test.

## Summary

Ghost Karts is a single-page browser game: drive a kart around a lantern-lit loop, beat your best lap, and race against the saved "ghost" of a previous best run. Everything is drawn in code inside one HTML file.

## What's inside

- `index.html`: the whole game (HTML, CSS and JavaScript), with no build step and no external assets.
- `test.py`: an optional headless Playwright smoke test. It drives a couple of laps automatically, checks that a ghost lap is saved, reports any page errors, and writes a screenshot.
- `shot.png`: a screenshot produced by the smoke test.
- `LICENSE`: the MIT license.

## How to play or run it

- **Online:** open the Play link above.
- **Locally:** download or clone the repo and open `index.html` in a modern browser.
- **Smoke test (optional):** `pip install playwright`, then run `python test.py` from the repo folder. The script launches Chrome from `/usr/bin/google-chrome`, so adjust that path if yours is somewhere else.

## License

MIT, see [LICENSE](LICENSE).
