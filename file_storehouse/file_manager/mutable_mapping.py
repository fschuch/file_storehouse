"""Bucket manager, the core of file-storehouse."""

from collections.abc import MutableMapping
from typing import Any

from .mapping import FileManagerReadOnly


class FileManager(FileManagerReadOnly, MutableMapping):
    """Summary."""

    def __setitem__(self, key: Any, file_content: Any) -> None:
        """Upload a file to the client associated to the given key."""
        engine_key = self._get_engine_key(key)

        _file_content = file_content
        for transformation in reversed(self.transformation_list):
            _file_content = transformation.convert_from_dict_to_engine(_file_content)

        self.engine.set_item(engine_key, _file_content)

    def __delitem__(self, key: Any) -> None:
        """Delete a file from the client associated to the given id."""
        engine_key = self._get_engine_key(key)
        self.engine.delete_item(engine_key)
