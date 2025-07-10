"""Raw key mapping."""

from dataclasses import dataclass

from file_storehouse.key_mapping.base import KeyMappingABC
from file_storehouse.type import PathLike


@dataclass(frozen=True, eq=True)
class KeyMappingRaw(KeyMappingABC):
    """Raw key mapping."""

    def get_dict_key_from_engine(self, engine_key: PathLike) -> PathLike:
        """
        Compute a Python dictionary's key from an object's key at the engine.

        Parameters
        ----------
        engine_key : str
            Key of the object at the engine.

        Returns
        -------
        PathLike
            Key of the Python dictionary.
        """
        return engine_key

    def get_engine_key_from_dict(self, dict_key: PathLike) -> PathLike:
        """
        Compute an object's key at the engine from a Python dictionary's key.

        Parameters
        ----------
        dict_key : Any
            Key of the Python dictionary.

        Returns
        -------
        str
            Key of the object at the engine.
        """
        return dict_key
