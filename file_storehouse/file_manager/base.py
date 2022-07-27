"""Bucket manager, the core of file-storehouse."""

from dataclasses import dataclass, field
from typing import List

from file_storehouse.engine.base import EngineABC
from file_storehouse.key_mapping.base import KeyMappingABC
from file_storehouse.key_mapping.raw import KeyMappingRaw
from file_storehouse.transformation.base import TransformationABC


@dataclass(eq=False)
class FileManagerData:
    """Dataclass containing the properties of a S3 manager."""

    engine: EngineABC
    transformation_list: List[TransformationABC] = field(default_factory=list)
    key_mapping: KeyMappingABC = field(default_factory=KeyMappingRaw)
