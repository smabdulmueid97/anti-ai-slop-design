---
name: anti-ai-slop-design
description: Stop shipping generic AI-looking UI — spot the tells, pick a real visual direction, and run a slop check before you finish.
---

# Anti-AI-Slop Design

Use this skill whenever you are about to build, redesign, or review a user
interface — a landing page, a dashboard, a marketing site, a component.
Invoke it **before** you write the layout, not after. It exists for one
reason: most AI-generated UI looks the same, and users can tell in under a
second.

## What "AI slop" looks like

Slop is not bad code. It is a design that could belong to any product. Learn
the tells. If your output matches three or more of them, it is slop.

**The visual tells**

- **The violet-to-blue gradient.** A diagonal purple-to-blue wash across the
  hero, the buttons, the background, or all three. It is the single most
  common giveaway. Gradients are fine as a deliberate choice; a gradient as
  the whole identity is not a choice.
- **Inter everywhere.** Inter as the only font, at the default weights, at
  the default sizes. It is a good typeface. It is also the default, which
  means it reads as "nobody chose a typeface."
- **The same layout, every time.** Centered hero, a short eyebrow label,
  a big headline, a subhead, two buttons, then a row of exactly three
  feature cards, then a stats band, then a testimonial, then a footer.
  If the layout would fit any product with a find-and-replace, it is slop.
- **An eyebrow label above every heading.** A tiny uppercase line with wide
  letter-spacing sitting over each section title, like a label on a label.
  Used once it is emphasis. Used five times it is wallpaper.
- **Tracked-out uppercase labels.** Small caps with heavy letter-spacing
  used for ordinary body copy or for words that do not need shouting.
- **The big-number stat block.** "10,000+ users · 99.9% uptime · 4.9 rating"
  in three columns, big number over small grey label, with no source and
  no context. Numbers without proof are decoration.
- **Glassmorphism everywhere.** Frosted panels, blurred backdrops, and
  translucent cards stacked on a gradient, whether or not anything needs
  to be translucent.
- **A rounded-square icon above every heading.** A soft square with a
  generic glyph, repeated in every card, every section, every feature.
  Icons should mean something specific, not fill a slot.
- **Generic stock imagery.** Smiling people at laptops, abstract 3D
  shapes, a handshake, a skyline. If the image could illustrate a
  hundred different products, it illustrates none of them.
- **Empty decorative frames.** Browser chrome drawn around nothing,
  dashboard mockups with grey bars where content should be, placeholder
  rectangles pretending to be a product.

**The copy tells**

- **The same verbs.** Delve, elevate, unlock, seamless, supercharge,
  empower, revolutionize. If a sentence could appear on any SaaS homepage,
  it says nothing about this product.
- **Emoji bullets.** A list where every line starts with ✨, 🚀, or ✅
  instead of a real point. Emojis are not evidence.
- **Vague claims.** "AI-powered", "next-generation", "cutting-edge" with
  no concrete feature, number, or example attached.

**The behaviour tells**

- **Content hidden until JavaScript reveals it.** Text that starts at
  `opacity: 0` and only appears after a scroll animation. If JavaScript
  fails, the page is blank. Content should be visible by default;
  animation is a bonus, never a gate.

## The fix process

Do this in order, before you write the layout.

### 1. Pick a real visual direction first

Answer these three questions in writing, before any code:

- **Type:** one distinctive pairing — a characterful display face for
  headings plus a readable face for body. Two faces, max. Name them and
  say why they fit this product. If you cannot say why, you have not
  chosen, you have defaulted.
- **Colour:** one restrained palette with one real accent. A background,
  a surface, a text colour, and one accent that is used sparingly — for
  the primary action and for emphasis, nowhere else. No gradient as the
  identity. If the palette needs a gradient to look finished, the palette
  is unfinished.
- **Content:** write the real words first. The headline should name the
  specific thing this product does and who it is for. If the headline
  works for a different product, rewrite it until it does not.

### 2. Design rules

- **Type scale:** pick a scale (for example 12 / 14 / 16 / 20 / 24 / 32 /
  48) and stick to it. Do not invent a new size per element.
- **Spacing:** pick a spacing scale (for example 4 / 8 / 16 / 24 / 32 /
  48 / 64) and stick to it. Rhythm comes from repetition, not from
  eyeballing each gap.
- **Contrast:** body text must meet at least 4.5:1 contrast against its
  background. Small grey text on a light background is the most common
  readability failure in generated UI.
- **One accent only.** One accent colour, used for the primary action
  and for emphasis. Everything else is neutral. Two accents is a
  second brand.
- **No gradient as a crutch.** A gradient may appear as one deliberate
  element, never as the background, the buttons, and the cards at once.
- **Real imagery or honest illustration.** Use a real photo of the
  actual product, a real screenshot, or a simple illustration made for
  this page. Never a generic stock photo. If no real image exists, a
  clean typographic layout beats a fake one.
- **Copy that says something specific.** Every headline and every
  feature must name a concrete outcome, a concrete user, or a concrete
  number with a source. Cut any sentence that survives a find-and-replace
  onto a competitor's site.
- **Layout follows content.** Choose the layout after the content
  exists. If the content is one strong idea, one strong section may be
  enough. Do not pad a page with a three-card row, a stats band, and a
  testimonial section it does not need.
- **Visible by default.** Content is in the document and visible without
  JavaScript. Animations add polish; they never gate readability.

### 3. The slop check — run it before you finish

Before you call the work done, run the checklist below on your own
output. Every item is yes/no. Any "no" is a fix, not a note.

1. Could this page belong to a different product with a find-and-replace? (must be no)
2. Is there a violet-to-blue gradient used as the identity? (must be no)
3. Is Inter the only font, at default weights and sizes? (must be no)
4. Is the layout the default hero + three cards + stats band? (must be no)
5. Is there an eyebrow label above more than one heading? (must be no)
6. Is tracked-out uppercase used for anything that is not a real label? (must be no)
7. Are there big-number stats with no source? (must be no)
8. Is glassmorphism used on more than one element? (must be no)
9. Is there a rounded-square icon above a heading that adds no meaning? (must be no)
10. Is the imagery generic stock, or could it illustrate any product? (must be no)
11. Are there empty decorative frames or placeholder mockups? (must be no)
12. Does the copy use delve, elevate, unlock, seamless, or supercharge? (must be no)
13. Does any list rely on emoji bullets instead of real points? (must be no)
14. Is there a vague claim ("AI-powered", "next-generation") with no concrete detail? (must be no)
15. Is any content hidden at `opacity: 0` until JavaScript reveals it? (must be no)
16. Does body text meet 4.5:1 contrast? (must be yes)
17. Is there exactly one accent colour, used sparingly? (must be yes)
18. Does the headline name the specific product and its specific user? (must be yes)
19. Is every section there because the content needs it, not because the template has a slot? (must be yes)
20. Would you recognise this page if the logo were removed? (must be yes)

If you cannot honestly answer yes to 16–20 and no to 1–15, fix the
output. Do not explain the slop away.

## How to use this skill in Claude Code

- **Before building UI:** invoke `/anti-ai-slop-design` and describe the
  page. Answer the three direction questions (type, colour, content)
  first, then build.
- **In a project:** copy this folder into `.claude/skills/` or add it
  with `claude skills add` so it applies to every UI task in the repo.
- **As a review:** paste the checklist into a review prompt and ask the
  agent to score its own output item by item, then fix every failure.
- **With the checker:** run `python scripts/slop-check.py <files>` for a
  fast deterministic pass on the obvious tells. It catches the mechanical
  ones; the checklist catches the judgement ones. Use both.
