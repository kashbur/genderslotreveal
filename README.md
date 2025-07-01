# The Big Reveal

This project contains a single HTML file that displays an interactive slot machine-style reveal. Spinning the reels a few times eventually triggers a personalized message overlay with optional confetti effects. It's designed for fun occasions like pregnancy announcements, graduations, or other surprises.

## Opening the page

You can open `index.html` directly in any modern web browser. Simply double-click the file or serve it through a local HTTP server and navigate to the page.

```
open index.html            # macOS
# or
xdg-open index.html        # Linux
```

## Customizing via URL parameters

`index.html` supports several query parameters so you can customize the reveal text and appearance. Parameters are optional and can be combined:

- `main` – main headline (default: "We're Expecting!")
- `sub` – secondary line of text
- `date` – additional date or detail line
- `photo` – URL to an image shown as a circular avatar
- `from` – a closing signature line
- `color` – overlay color when the message appears. Allowed values: `beige` (default), `pink`, `blue`, `yellow`, `green`, `purple`, `gold`, `none`.

### Example links

```
index.html?main=We%27re%20Engaged!&sub=Save%20the%20Date&date=June%202024
```

```
index.html?main=It%27s%20a%20Boy%21&photo=https%3A%2F%2Fexample.com%2Fbaby.jpg&from=Love%2C%20Alice%20and%20Bob&color=blue
```

Open one of these URLs in your browser to see the customized reveal.
