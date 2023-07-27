# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------
import sys

# Docs require Python 3.6+ to generate
from pathlib import Path

DIR = Path(__file__).parent.parent.parent.resolve()
BASEDIR = DIR.parent

sys.path.append(str(BASEDIR / "src"))

# -- Project information -----------------------------------------------------

project = "Modelspec"
copyright = "2023, ModECI Project"
author = "ModECI Project"
release = "0.3.1"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",  # auto generate docstrings
    "sphinx.ext.autosummary",  # auto generate summary tables
    "sphinx.ext.napoleon",  # napoleon docstring style
    # "sphinx.ext.mathjax",
    "sphinx_copybutton",  # create copy buttons
    "sphinx_rtd_theme",  # html theme
    "sphinx_markdown_tables",  # include markdown style tables
    # "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosectionlabel",
    # "sphinx.ext.todo",
    "myst_parser",
    "sphinx.ext.githubpages",
]

autodoc_member_order = "bysource"
autosummary_generate = True
autoclass_content = "both"  # Add __init__ doc (ie. params) to class summaries
html_show_sourcelink = (
    False  # Remove 'view source code' from top of page (for html, not python)
)

master_doc = "index"
napoleon_use_ivar = True
autosectionlabel_prefix_document = True

# Source Suffix
source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "restructuredtext",
    ".md": "markdown",
}

source_parsers = {".md": "myst_parser"}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
