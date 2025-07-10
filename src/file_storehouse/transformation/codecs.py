"""Codecs transformations."""

from codecs import decode, encode
from dataclasses import dataclass

from file_storehouse.transformation.base import TransformationABC
from file_storehouse.type import FileLike


@dataclass(frozen=True, eq=True)
class TransformationCodecs(TransformationABC):
    """Support for encode/decode transformations."""

    encoding_name: str = "utf-8"

    def convert_from_engine_to_dict(self, file_content: bytes) -> FileLike:
        """From engine to dict."""
        return decode(file_content, encoding=self.encoding_name)

    def convert_from_dict_to_engine(self, file_content: str) -> FileLike:
        """From dict to engine."""
        return encode(file_content, encoding=self.encoding_name)
