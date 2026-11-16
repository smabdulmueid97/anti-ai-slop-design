# anti-ai-slop-design

A Claude Code skill that stops a coding agent from shipping generic
AI-looking UI. Most AI-generated interfaces look the same — same gradient,
same font, same three cards — and users can tell in under a second. This
skill teaches the agent to spot the tells, pick a real visual direction,
and run a check on its own output before it calls the work done.

## The tells it kills

- Violet-to-blue gradients used as the whole identity
- Inter as the only font, at default weights and sizes
- The default layout: centered hero, three feature cards, stats band
- Eyebrow labels above every heading, tracked-out uppercase everywhere
- Big-number stat blocks with no source
- Glassmorphism on everything, rounded-square icons above every heading
- Generic stock imagery and empty decorative frames
- Copy full of delve, elevate, unlock, seamless, supercharge
- Emoji bullets instead of real points
- Content hidden at `opacity: 0` until JavaScript reveals it

## What's inside

- `SKILL.md` — the skill: the tells, the fix process (direction first,
  then design rules, then the review pass), and a 20-item slop checklist.
- `scripts/slop-check.py` — a small deterministic checker (Python, no
  dependencies). Scans HTML/CSS for the mechanical tells and prints
  PASS/FAIL per check with file and line number.
- `examples/slop.html` — a deliberately sloppy AI-default landing page.
- `examples/fixed.html` — the same page redesigned following the skill's
  rules. Open both in a browser: the difference is visible in seconds.

## Install

Copy this folder into your Claude Code skills directory, or add it with:

```bash
claude skills add /path/to/anti-ai-slop-design
```

Then invoke it before building UI:

```
/anti-ai-slop-design
```

Or paste the checklist from `SKILL.md` into a review prompt and ask the
agent to score its own output, then fix every failure.

## Run the checker

```bash
python scripts/slop-check.py examples/slop.html examples/fixed.html
```

`slop.html` fails with a list of tells; `fixed.html` passes. The checker
catches the mechanical tells — the checklist in `SKILL.md` catches the
judgement ones. Use both.

## Before / after

- **Before** (`examples/slop.html`): purple-blue gradient hero, Inter
  everywhere, eyebrow label, three glass cards with emoji bullets,
  unsourced "10,000+ users" stats, content hidden until JS runs.
- **After** (`examples/fixed.html`): one distinctive typeface pairing
  (Fraunces + Newsreader), one accent colour, real words first, concrete
  pricing, a named team behind it, visible without JavaScript.

## License

MIT — see `LICENSE`.
