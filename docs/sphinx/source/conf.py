# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


# -- Path setup -------------------------------------------------------------
import sys
import os
from pathlib import Path

DIR = Path(__file__).parent.parent.parent.resolve()
BASEDIR = DIR.parent

sys.path.append(os.path.join(BASEDIR, "src"))

project = "modelspec"
copyright = "2023, ModECI project"
author = "ModECI project"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",  # auto generate docstrings
    "sphinx.ext.autosummary",  # auto generate summary tables
    "sphinx_rtd_theme",  # html theme
    "sphinx.ext.napoleon",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.githubpages",
    "recommonmark",
]

autodoc_member_order = "bysource"
autosummary_generate = (
    True  # auto generate summary tables for objects listed in the autosummary directive
)
autoclass_content = "both"
napoleon_use_ivar = True
autosectionlabel_prefix_document = True
html_show_sourcelink = (
    False  # Remove 'view source code' from top of page (for html, not python)
)

# Source Suffix
source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "restructuredtext",
    ".md": "markdown",
}

source_parsers = {".md": "recommonmark.parser.CommonMarkParser"}

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster' #commented code
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
