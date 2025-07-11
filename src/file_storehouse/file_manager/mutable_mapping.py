"""Bucket manager, the core of file-storehouse."""

from collections.abc import MutableMapping
from typing import Any

from .mapping import FileManagerReadOnly


class FileManager(FileManagerReadOnly, MutableMapping):
    """
    File manager with read and write access.

    It implements the ``MutableMapping`` protocol, alloying the users to access files
    using a friendly dict-like interface.

    Parameters
    ----------
    engine : EngineABC
        Back-end file engine.
    io_transformations : Tuple[TransformationABC, ...]
        A container describing the transformations to be applied to the objects when
        manipulating them back and forward the back-end engine. They are given in the
        same order they are expected to be applied when loading the files.
    key_mapping : KeyMappingABC
        The ``key_mapping`` translates back and forward the key used in the dictionary
        to the absolute path used to access the files from the engine.

    Notes
    -----
    For the ``Mapping`` protocol and read-only protection, see
    ``file_storehouse.FileManagerReadOnly``.
    """

    def __setitem__(self, key: Any, file_content: Any) -> None:
        """Upload a file to the client associated to the given key."""
        engine_key = self._get_engine_key(key)

        _file_content = file_content
        for transformation in reversed(self.io_transformations):
            _file_content = transformation.convert_from_dict_to_engine(_file_content)

        self.engine.set_item(engine_key, _file_content)

    def __delitem__(self, key: Any) -> None:
        """Delete a file from the client associated to the given id."""
        engine_key = self._get_engine_key(key)
        self.engine.delete_item(engine_key)
