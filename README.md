# Academic Portfolio

Personal academic website built with [MyST Markdown](https://myst-parser.readthedocs.io/) and [Sphinx](https://www.sphinx-doc.org/), deployed to GitHub Pages via GitHub Actions.

## Quickstart

```bash
pip install -r requirements.txt
sphinx-build -b html docs docs/_build
```

Open `docs/_build/index.html` in your browser.

## Structure

```
docs/
├── index.md         # Home page
├── about.md         # About me
├── cv.md            # CV / Resume
├── research/        # Research projects
├── projects/        # Other projects
├── publications/    # Publications (BibTeX)
├── teaching/        # Teaching experience
├── blog/            # Blog posts
├── gallery/         # Photo gallery
├── contact.md       # Contact info
├── conf.py          # Sphinx configuration
└── _static/         # Custom CSS/images
```

## Deployment

Push to `main` — GitHub Actions builds and deploys to GitHub Pages automatically.
# birhanu-academic-portfolio
