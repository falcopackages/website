# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'falcoproject'
copyright = '2024, Tobi DEGNON'
author = 'Tobi DEGNON'
release = '2024'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.extlinks",
    "myst_parser",
    "sphinx.ext.todo",
    "sphinx.ext.autodoc",
    "sphinx_design",
    "sphinx_tabs.tabs",
    "sphinx_copybutton",
    "sphinx_togglebutton",
    "sphinxcontrib.mermaid",
    # "sphinx_docsearch",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

todo_include_todos = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "shibuya"
html_static_path = ['_static']
html_baseurl = "https://falco.oluwatobi.dev"
html_title = "falcoproject"

# -- Shibuya theme options ---------------------------------------------------
html_context = {
    "source_type": "github",
    "source_user": "falcopackages",
    "source_repo": "website",
}

html_theme_options = {
    "mastodon_url": "https://fosstodon.org/@tobide",
    "github_url": "https://github.com/falcopackages",
    "twitter_url": "https://twitter.com/tobidegnon",
    "discussion_url": "https://github.com/orgs/falcopackages/discussions",
    "accent_color": "blue",
    "announcement": "Looking for the legacy documentation? Visit <a href='https://legacy.falcoproject.com'>this link</a>",
    "globaltoc_expand_depth": 1,
    "nav_links": [
        {"title": "Home", "url": "index"},
        {
            "title": "Community",
            "children": [
                {
                    "title": "GitHub Discussions",
                    "summary": "GitHub Discussions",
                    "url": "https://github.com/falcopackages/falco-app/discussions",
                    "icon": "coc",
                },
                {
                    "title": "Contributing",
                    "summary": "Learn how to contribute to the falco project",
                    "url": "contributing",
                    "icon": "contributing",
                },
                {
                    "title": "Code of Conduct",
                    "summary": "Review the etiquette for interacting with the falco community",
                    "url": "codeofconduct",
                    "icon": "coc",
                },
            ],
        },
        {
            "title": "Support",
            "url": "https://buymeacoffee.com/oluwa.tobi",
            "icon": "heart",
        },
    ],
}
html_logo = "_static/logo_with_text.svg"
html_favicon = "_static/falco-logo.svg"
html_css_files = [
    "custom.css",
]
html_sidebars = {
    "**": [
        "sidebars/localtoc.html",
        "sidebars/repo-stats.html",
        "sidebars/edit-this-page.html",
        "sidebars/consulting.html",
        # "sidebars/buy-me-a-coffee.html",
    ]
}

html_js_files = [
    (
        "https://plausible.service.dotfm.me/js/script.js",
        {"defer": "", "data-domain": "falco.oluwatobi.dev"},
    ),
    "add-og-title-to-home.js",
    (
        "https://cdnjs.buymeacoffee.com/1.0.0/widget.prod.min.js",
        {
            "data-name": "BMC-Widget",
            "data-cfasync": "false",
            "data-id": "oluwa.tobi",
            "data-description": "Support me on Buy me a coffee!",
            "data-message": "",
            "data-color": "#5F7FFF",
            "data-position": "Right",
            "data-x_margin": "18",
            "data-y_margin": "18",
        },
    ),
]

# -- DocSearch configs -----------------------------------------------------
docsearch_app_id = "CJEHOB5X2Y"
docsearch_api_key = "e467f62765922e10749dec55f81a0a76"
docsearch_index_name = "falco"
