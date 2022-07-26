"""Some examples for tests."""

from myproject import __version__


def test_version():
    """Test if the version is correct."""
    assert __version__ == "0.1.0"
