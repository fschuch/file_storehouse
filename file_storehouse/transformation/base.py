"""Convert file content back and forward."""

from abc import ABC, abstractmethod
from typing import Any


class TransformationABC(ABC):
    """Base for transformations."""

    @abstractmethod
    def convert_from_engine_to_dict(self, input: Any) -> Any:
        """From engine to dict."""
        pass

    @abstractmethod
    def convert_from_dict_to_engine(self, input: Any) -> Any:
        """From dict to engine."""
        pass
