"""Base class for the two way key mapping between dictionary key and the engine key."""

from abc import ABC, abstractmethod
from typing import Any

from file_storehouse.type import PathLike


class KeyMappingABC(ABC):
    """Describe how to convert dictionary keys to objects' keys at S3 and vice versa."""

    @abstractmethod
    def get_dict_key_from_engine(self, engine_key: PathLike) -> Any:
        """
        Compute a Python dictionary's key from an object's key at the engine.

        Parameters
        ----------
        engine_key : PathLike
            Key of the object at the engine.

        Returns
        -------
        Any
            Key of the Python dictionary.
        """
        pass

    @abstractmethod
    def get_engine_key_from_dict(self, dict_key: Any) -> PathLike:
        """
        Compute an object's key at the engine from a Python dictionary's key.

        Parameters
        ----------
        dict_key : Any
            Key of the Python dictionary.

        Returns
        -------
        PathLike
            Key of the object at the engine.
        """
        pass
