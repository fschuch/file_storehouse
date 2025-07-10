"""File manager, the core of file-storehouse."""

from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Any, Iterator, Tuple

from file_storehouse.engine.base import EngineABC
from file_storehouse.key_mapping.base import KeyMappingABC
from file_storehouse.key_mapping.raw import KeyMappingRaw
from file_storehouse.transformation.base import TransformationABC


@dataclass(frozen=True, eq=False)
class FileManagerReadOnly(Mapping):
    """
    File manager with read only properties.

    It implements the ``Mapping`` protocol, alloying the users to access files using
    a friendly dict-like interface.

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
    For the ``MutableMapping`` protocol and writhing capabilities, see
    ``file_storehouse.FileManager``.
    """

    engine: EngineABC
    io_transformations: Tuple[TransformationABC, ...] = field(default_factory=tuple)
    key_mapping: KeyMappingABC = field(default_factory=KeyMappingRaw)

    def __getitem__(self, key: Any) -> Any:
        """
        Get from the file engine the object associated to the given key.

        Parameters
        ----------
        key : Any
            Dictionary key, that is translated internally to the engine absolute path
            according to the ``key_mapping``.

        Returns
        -------
        Any
            The object resulting from the ``io_transformations``.

        Raises
        ------
        KeyError
            If there is no object associated with the given key.
        """
        engine_key = self._get_engine_key(key)
        result = self.engine.get_item(engine_key)
        for transformation in self.io_transformations:
            result = transformation.convert_from_engine_to_dict(result)
        return result

    def __iter__(self) -> Iterator[Any]:
        """Yield the keys found in the working folder."""
        for key in self.engine.list_keys():
            yield self._get_dict_key(key)

    def __len__(self) -> int:
        """Count the number of keys found in the working folder."""
        return sum(1 for _ in self)

    def _get_engine_key(self, dict_key: Any) -> Any:
        return self.engine.convert_to_absolute_path(
            self.key_mapping.get_engine_key_from_dict(dict_key)
        )

    def _get_dict_key(self, engine_key: Any) -> Any:
        return self.key_mapping.get_dict_key_from_engine(
            self.engine.convert_to_relative_path(engine_key)
        )
