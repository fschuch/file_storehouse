"""
Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import os

import toml  # type: ignore

project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
toml_data = toml.load(os.path.join(project_root, "pyproject.toml"))
project_metadata = toml_data["tool"]["poetry"]
project_metadata["author"] = project_metadata["authors"][0]

# -- Project information -----------------------------------------------------

project = project_metadata["name"]
copyright = "2022, Felipe N. Schuch"
author = project_metadata["author"]

# The full version, including alpha/beta/rc tags
version = project_metadata["version"]
release = project_metadata["version"]


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx_last_updated_by_git",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "boto3": ("https://boto3.amazonaws.com/v1/documentation/api/latest/", None),
    "botocore": ("https://botocore.readthedocs.io/en/latest/", None),
}
extlinks = {
    "boto3": (
        "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/%s",
        None,
    ),
}

# Enable Google-style docstrings
napoleon_numpy_docstring = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns: list = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
