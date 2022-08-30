"""Engine for S3 buckets."""

from dataclasses import dataclass
from pathlib import PurePath
from typing import Iterator

from botocore.client import BaseClient

from file_storehouse.engine.base import EngineABC
from file_storehouse.type import PathLike


@dataclass(frozen=True, eq=True)
class EngineS3(EngineABC):
    """Engine for S3 buckets."""

    s3_client: BaseClient
    bucket_name: str
    prefix: str = ""

    def get_item(self, key: str) -> bytes:
        """Get the item related to the key."""
        try:
            response = self.s3_client.get_object(Bucket=self.bucket_name, Key=key)
        except self.s3_client.exceptions.NoSuchKey:
            raise KeyError(f"No such {key=}")

        return response["Body"].read()

    def set_item(self, key: str, file_content: bytes) -> None:
        """Set the item related to the key."""
        try:
            self.s3_client.put_object(
                Body=file_content, Bucket=self.bucket_name, Key=key
            )
        except self.s3_client.exceptions.NoSuchKey:
            raise KeyError(f"No such {key=}")

    def delete_item(self, key: str) -> None:
        """Delete the item related to the key."""
        try:
            self.s3_client.delete_object(Bucket=self.bucket_name, Key=key)
        except self.s3_client.exceptions.NoSuchKey:
            raise KeyError(f"No such key {key=}")

    def list_keys(self) -> Iterator[PathLike]:
        """List the keys related to the engine."""
        paginator = self.s3_client.get_paginator("list_objects_v2")
        for page in paginator.paginate(Bucket=self.bucket_name, Prefix=self.prefix):
            contents = page.get("Contents", [])
            if not contents:
                break
            for obj in contents:
                yield obj["Key"]

    def ensure_bucket(self):
        """Ensure that the bucket exists. Skip creation if it already exists."""
        try:
            self.s3_client.create_bucket(Bucket=self.bucket_name)
        except self.s3_client.exceptions.BucketAlreadyOwnedByYou:
            pass

    def convert_to_absolute_path(self, relative_path: PathLike) -> str:
        """Convert to absolute path."""
        return str(PurePath(self.prefix, relative_path))

    def convert_to_relative_path(self, absolute_path: str) -> PathLike:
        """Convert to relative path."""
        return PurePath(absolute_path).relative_to(self.prefix)
