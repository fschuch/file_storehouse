"""Engine for the local file system."""

from dataclasses import dataclass
from pathlib import Path
from typing import Iterator

from file_storehouse.engine.base import EngineABC
from file_storehouse.type import PathLike


@dataclass(frozen=True, eq=True)
class EngineLocal(EngineABC):
    """Engine for the local file system."""

    base_path: Path

    def get_item(self, key: Path) -> bytes:
        """Get the item related to the key."""
        if key.is_file():
            return key.read_bytes()
        raise KeyError(f"No such key {key=}")

    def set_item(self, key: Path, file_content: bytes) -> None:
        """Set the item related to the key."""
        key.parent.mkdir(parents=True, exist_ok=True)
        key.write_bytes(file_content)

    def delete_item(self, key: Path) -> None:
        """Delete the item related to the key."""
        if key.is_file():
            key.unlink()
        else:
            raise KeyError(f"No such key {key=}")

        self._remove_empty_folders(key)

    def list_keys(self) -> Iterator[PathLike]:
        """List the keys related to the engine."""
        return (path for path in self.base_path.rglob("*") if path.is_file())

    def convert_to_absolute_path(self, relative_path: PathLike) -> Path:
        """Convert to absolute path."""
        return Path(self.base_path, relative_path).resolve()

    def convert_to_relative_path(self, absolute_path: Path) -> Path:
        """Convert to relative path."""
        return Path(absolute_path).relative_to(self.base_path)

    def _remove_empty_folders(self, key: Path) -> None:
        """Remove folders in the path that become empty."""
        rel_path = Path(key)
        while rel_path != self.base_path:
            try:
                rel_path.rmdir()
            except OSError:
                break
            rel_path = rel_path.parent
