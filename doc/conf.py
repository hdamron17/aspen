PROJECT_ROOT = ".."

import os
import sys
sys.path.insert(0, os.path.abspath(PROJECT_ROOT))

project = "mulberry"
copyright = "2020, Hunter Damron"
author = "Hunter Damron"

with open(os.path.join(PROJECT_ROOT, "VERSION"), "r") as fh:
    release = fh.read().strip()
    version = ".".join(release.split(".")[:2])  # Get major version

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
]

templates_path = ["_templates"]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "alabaster"

html_static_path = ["_static"]
