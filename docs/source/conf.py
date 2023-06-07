# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# Docs require Python 3.6+ to generate
from pathlib import Path

DIR = Path(__file__).parent.parent.parent.resolve()
BASEDIR = DIR.parent

sys.path.append(str(BASEDIR / "src"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'modelspec'
copyright = '2023, ModECI contributors'
author = 'ModECI contributors'
release = '0.3.0'

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

templates_path = ['_templates']
exclude_patterns = [
    
]

autodoc_member_order = "bysource"
autosummary_generate = True
autoclass_content = "both"  # Add __init__ doc (ie. params) to class summaries
html_show_sourcelink = (
    False  # Remove 'view source code' from top of page (for html, not python)
)


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
#
html_theme = "sphinx_rtd_theme"

html_theme_options = {
    "collapse_navigation": False,
    "display_version": True,
    "logo_only": False,
    "navigation_depth": -1,
    "includehidden": True,
}

# Output file base name for HTML help builder.
htmlhelp_basename = "modelspecdoc"

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    "python": ("https://docs.python.org/", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    "pytest": ("https://docs.pytest.org/en/stable", None),
}

from sphinx.ext.autodoc import ClassLevelDocumenter, InstanceAttributeDocumenter


def add_directive_header(self, sig):
    ClassLevelDocumenter.add_directive_header(self, sig)

# Source Suffix
source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "restructuredtext",
    ".md": "markdown",
}
InstanceAttributeDocumenter.add_directive_header = add_directive_header


import os

on_rtd = os.environ.get("READTHEDOCS", None) == "True"
if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme

    html_theme = "sphinx_rtd_theme"
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_css_files = ["rtd-custom.css"]  # Override some CSS settings
