"""Base for engine."""

from abc import ABC, abstractmethod
from typing import Any, Iterator

from ..type import FileLike, PathLike


class EngineABC(ABC):
    """Base for engine."""

    @abstractmethod
    def get_item(self, key: PathLike) -> FileLike:
        """Get the item related to the key."""
        pass

    @abstractmethod
    def set_item(self, key: PathLike, file_content: FileLike) -> None:
        """Set the item related to the key."""
        pass

    @abstractmethod
    def delete_item(self, key: PathLike) -> None:
        """Delete the item related to the key."""
        pass

    @abstractmethod
    def list_keys(self) -> Iterator[PathLike]:
        """List the keys related to the engine."""
        pass

    @abstractmethod
    def convert_to_absolute_path(self, relative_path: PathLike) -> Any:
        """Convert to absolute path."""
        pass

    @abstractmethod
    def convert_to_relative_path(self, absolute_path: Any) -> PathLike:
        """Convert to relative path."""
        pass
