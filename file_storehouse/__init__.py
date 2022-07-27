"""File-storehouse package."""

from .extras import Stubber, client
from .file_manager.mapping import FileManagerReadOnly
from .file_manager.mutable_mapping import FileManager

__all__ = [
    "client",
    "Stubber",
    "FileManager",
    "FileManagerReadOnly",
]
