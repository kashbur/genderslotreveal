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

- `main` – main headline (default: "We are expecting!")
- `sub` – secondary line of text
- `date` – additional date or detail line
- `photo` – URL to an image shown as a circular avatar
- `from` – a closing signature line
- `color` – overlay color when the message appears. Allowed values: `beige` (default), `pink`, `blue`, `yellow`, `green`, `purple`, `gold`, `white`, `none`. You can also supply any valid hex or CSS color value for a custom overlay.
- `textColor` – color for the message text (any valid CSS color value)
- `outlineColor` – color for the outline around the message text
- `font` – Google Fonts family name to use for all text (e.g. `font=Playfair+Display`)

`color` only affects the overlay background, whereas `textColor` and `outlineColor` control the message text and its outline.

### Example links

```
index.html?main=We%27re%20Engaged!&sub=Save%20the%20Date&date=June%202024
```

```
index.html?main=We%E2%80%99re%20expecting&font=Playfair+Display
```

```
index.html?main=It%27s%20a%20Boy%21&photo=https%3A%2F%2Fexample.com%2Fbaby.jpg&from=Love%2C%20Alice%20and%20Bob&color=coral
```

```
index.html?main=We%27re%20expecting%21&sub=Baby%20Miller%20%233&date=Arriving%20January%202026&photo=<url>&from=Love%2C%20Geoffrey%20and%20Kristina&color=beige&textColor=%23000000&outlineColor=%23888888
```

Open one of these URLs in your browser to see the customized reveal.
