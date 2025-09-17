from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version(__package__)
except PackageNotFoundError:
    __version__ = "na"


from eralchemy import render_er

__all__ = ("render_er", "__version__")
