project = "Birhanu's Academic Portfolio"
copyright = "2024, Birhanu"
author = "Birhanu"

extensions = [
    "myst_parser",
    "sphinx_book_theme",
    "sphinx_design",
    "sphinxcontrib.bibtex",
    "sphinx.ext.mathjax",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinxext.opengraph",
    "sphinx_copybutton",
    "sphinx_sitemap",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "deflist",
    "html_image",
    "colon_fence",
    "smartquotes",
    "replacements",
    "linkify",
    "substitution",
]

myst_heading_anchors = 3

bibtex_bibfiles = ["publications.bib"]
bibtex_default_style = "unsrt"
bibtex_reference_style = "author_year"

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "publications.bib"]

html_theme = "sphinx_book_theme"
html_title = "Birhanu"
html_logo = ""
html_favicon = ""

html_theme_options = {
    "repository_url": "https://github.com/birhekobo/birhanu-academic-portfolio",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "home_page_in_toc": True,
    "show_toc_level": 2,
    "navigation_depth": 3,
    "path_to_docs": "docs",
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/birhekobo",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "Google Scholar",
            "url": "https://scholar.google.com/citations?user=XXX",
            "icon": "fa-brands fa-google-scholar",
        },
        {
            "name": "ORCID",
            "url": "https://orcid.org/0000-0000-0000-0000",
            "icon": "fa-brands fa-orcid",
        },
        {
            "name": "LinkedIn",
            "url": "https://linkedin.com/in/birhekobo",
            "icon": "fa-brands fa-linkedin",
        },
    ],
}

html_static_path = ["_static"]
html_css_files = ["custom.css"]

pygments_style = "sphinx"

suppress_warnings = [
    "toc.not_included",
    "design.grid",
    "myst.directive_option",
    "bibtex.duplicate_label",
]

ogp_site_url = "https://birhekobo.github.io/birhanu-academic-portfolio"
ogp_description_length = 200
ogp_enable_social_cards = False

html_baseurl = "https://birhekobo.github.io/birhanu-academic-portfolio"

sitemap_url_scheme = "{link}"
