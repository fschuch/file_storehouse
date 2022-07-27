"""File manager."""

from .mapping import FileManagerReadOnly
from .mutable_mapping import FileManager

__all__ = [
    "FileManager",
    "FileManagerReadOnly",
]
