# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# Add the project root and set Django settings
sys.path.insert(0, os.path.abspath("../../"))
os.environ["DJANGO_SETTINGS_MODULE"] = (
    "core.settings"  # Adjust this if your settings module is named differently
)

# Initialize Django
import django

django.setup()

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "one-with-the-force-api"
copyright = "2024, Giorgos Kalomalos"
author = "Giorgos Kalomalos"
release = "0.2.2"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",  # Automatically documents from docstrings
    "sphinx.ext.autosummary",  # Generates summaries for modules/classes
    "sphinx.ext.napoleon",  # Supports Google and NumPy style docstrings
    "sphinx.ext.viewcode",  # Links to source code
]

# Enable generation of `autosummary` documentation stubs
autosummary_generate = True


templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "**/migrations/*",  # Exclude migrations
    "tests/",  # Exclude tests
    "**/admin.py",  # Exclude admin config
    "**/settings.py",  # Exclude settings file
    "**/wsgi.py",  # Exclude WSGI file
    "**/asgi.py",  # Exclude ASGI file
]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
