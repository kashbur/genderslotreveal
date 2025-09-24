# The Big Reveal

This project contains a single HTML file that displays an interactive slot machine-style reveal. Spinning the reels a few times eventually triggers a celebratory message overlay with optional confetti effects. It's designed for fun occasions like pregnancy announcements or any other big surprise moments.

## Opening the page

You can open `index.html` directly in any modern web browser. Simply double-click the file or serve it through a local HTTP server and navigate to the page.

```
open index.html            # macOS
# or
xdg-open index.html        # Linux
```

## Customizing via URL parameters

`index.html` now recognizes just two optional query parameters so you can keep the experience simple:

- `gender` – set to `boy` or `girl` to trigger the matching celebratory overlay on the fourth spin. When omitted, the slot machine simply reveals the neutral surprise message.
- `lang` – choose the language used for the default messaging. The values `en`, `es`, `fr`, `de`, `pt`, `it`, `nl`, `sv`, and `ar` are supported, and region-specific variants such as `pt-BR` will fall back to their base language. The alias `language` is also accepted.

All other URL parameters are ignored.

### Example links

```
index.html?gender=girl
```

```
index.html?gender=boy&lang=es
```

```
index.html?lang=fr
```

Open one of these URLs in your browser to see the reveal tailored to your chosen gender and language.

## How the reel spinning works

The slot machine now shows a **1×3 grid** of icons. Each of the three columns is
a reel that spins vertically. When the spin button is pressed, the
`handleSpin()` function disables the button and calls `spinReel()` for each reel
using small delays so they start one after another. `spinReel()` builds a
vertical strip of random icons and applies the `spinning` CSS class, which runs
a `slot-spin-down` animation. After the configured duration, the class is
removed and `createSingleIcon()` displays the final symbol for that reel.

During the first three spins the grid stops on random symbols that never match
across all three reels. On the fourth spin all reels are forced to stop on the
bottle icon and `showReveal()` is triggered, revealing the celebratory message
overlay (and the gender announcement if you enabled it). Any spins after the
reveal go back to being completely random, so matches can happen naturally.
