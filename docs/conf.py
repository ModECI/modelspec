# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
from pathlib import Path

DIR = Path(__file__).parent.parent.parent.resolve()
BASEDIR = DIR.parent

sys.path.append(str(BASEDIR / "src"))

# sys.path.insert(0, os.path.abspath("../src"))

# -- Project information -----------------------------------------------------

project = "modelspec"
copyright = "2023, modeci contributors"
author = "modeci contributors"
release = "0.3.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",  # Core library for html generation from docstrings
    "sphinx.ext.autosummary",  # Create neat summary tables
    "sphinx.ext.napoleon",
    "sphinx.ext.mathjax",
    "sphinx_copybutton",
    "sphinx_rtd_theme",
    "sphinx_markdown_tables",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.todo",
    "myst_parser",
    "sphinx.ext.githubpages",
]

autodoc_member_order = "bysource"
autosummary_generate = True
autoclass_content = "both"  # Add __init__ doc (ie. params) to class summaries
html_show_sourcelink = (
    False  # Remove 'view source code' from top of page (for html, not python)
)

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
