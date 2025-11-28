"""{{ cookiecutter.project_name }}.

{{ cookiecutter.project_description }}
"""

try:
    from ._version import __version__
except ImportError:
    # Package not installed or version file not generated yet
    __version__ = "0.0.0.dev0"

__all__ = ["__version__"]
