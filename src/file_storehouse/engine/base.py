"""Base for engine."""

from abc import ABC, abstractmethod
from collections.abc import Iterator
from typing import Any

from ..type import PathLike


class EngineABC(ABC):
    """Base for engine."""

    @abstractmethod
    def get_item(self, key: Any) -> bytes:
        """Get the item related to the key."""

    @abstractmethod
    def set_item(self, key: Any, file_content: bytes) -> None:
        """Set the item related to the key."""

    @abstractmethod
    def delete_item(self, key: Any) -> None:
        """Delete the item related to the key."""

    @abstractmethod
    def list_keys(self) -> Iterator[PathLike]:
        """List the keys related to the engine."""

    @abstractmethod
    def convert_to_absolute_path(self, relative_path: PathLike) -> Any:
        """Convert to absolute path."""

    @abstractmethod
    def convert_to_relative_path(self, absolute_path: Any) -> PathLike:
        """Convert to relative path."""
