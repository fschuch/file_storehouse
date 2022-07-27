"""Bucket manager, the core of file-storehouse."""

from collections.abc import Mapping
from typing import Any, Iterator

from .base import FileManagerData


class FileManagerReadOnly(FileManagerData, Mapping):
    """
    Summary.

    Parameters
    ----------
    S3ManagerData : _type_
        _description_
    Mapping : _type_
        _description_
    """

    def __getitem__(self, key: Any) -> Any:
        """
        Get the object associated to the given key from the engine.

        Parameters
        ----------
        key : Any
            The keys are processed by the key_mapping.

        Returns
        -------
        Any
            _description_

        Raises
        ------
        KeyError
            If there is no object associated with the given key.
        """
        engine_key = self.key_mapping.get_engine_key_from_dict(key)
        result = self.engine.get_item(engine_key)
        for transformation in self.transformation_list:
            result = transformation.convert_from_engine_to_dict(result)
        return result

    def __iter__(self) -> Iterator[Any]:
        """Yield the keys found in the bucket."""
        for engine_key in self.engine.list_keys():
            yield self.key_mapping.get_dict_key_from_engine(engine_key)

    def __len__(self) -> int:
        """Count the number of keys found in the work folder."""
        return sum(1 for _ in self)
