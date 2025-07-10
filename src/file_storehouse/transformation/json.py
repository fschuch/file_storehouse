"""Json transformations."""

from dataclasses import dataclass, field
from json import dumps, loads
from typing import Any

from file_storehouse.transformation.base import TransformationABC


@dataclass(frozen=True, eq=True)
class TransformationJson(TransformationABC):
    """Support for json dump/load transformations."""

    dump_options: dict = field(default_factory=dict)
    load_options: dict = field(default_factory=dict)

    def convert_from_engine_to_dict(self, file_content: Any) -> Any:
        """From engine to dict."""
        return loads(file_content, **self.load_options)

    def convert_from_dict_to_engine(self, file_content: Any) -> Any:
        """From dict to engine."""
        return dumps(file_content, **self.dump_options)
