"""Numerated key mapping."""

from dataclasses import dataclass
from pathlib import Path

from file_storehouse.key_mapping.base import KeyMappingABC
from file_storehouse.type import PathLike


@dataclass(frozen=True, eq=True)
class KeyMappingNumeratedFolder(KeyMappingABC):
    """Numerated key mapping."""

    filename: str

    def get_dict_key_from_engine(self, engine_key: PathLike) -> int:
        """
        Compute a Python dictionary's key from an object's key at the engine.

        Parameters
        ----------
        engine_key : PathLike
             Key of the object at the engine.

        Returns
        -------
        int
            Key of the Python dictionary.
        """
        return int(Path(engine_key).parent.name)

    def get_engine_key_from_dict(self, dict_key: int) -> PathLike:
        """
        Compute an object's key at the engine from a Python dictionary's key.

        Parameters
        ----------
        dict_key : int
            Key of the Python dictionary.

        Returns
        -------
        PathLike
            Key of the object at the engine.
        """
        return Path(str(dict_key), self.filename)
