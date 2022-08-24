"""User story for an end-to-end test."""

import tempfile
from pathlib import Path
from sys import platform

from pytest import mark

import file_storehouse as s3
from file_storehouse.engine import EngineS3
from file_storehouse.engine.base import EngineABC
from file_storehouse.engine.local_file_system import EngineLocal
from file_storehouse.key_mapping import KeyMappingNumeratedFile
from file_storehouse.transformation import TransformationCodecs, TransformationJson


@mark.skipif(platform != "linux", reason="just runs on linux for now")
def test_s3_engine(docker_services):
    """S3 engine used to acceptance test."""
    client = s3.client(
        "s3",
        endpoint_url="http://localhost:9000",
        aws_access_key_id="compose-s3-key",
        aws_secret_access_key="compose-s3-secret",
    )

    engine = EngineS3(
        s3_client=client,
        bucket_name="file-storehouse-s3",
        prefix="products",
    )

    engine.ensure_bucket()

    run_acceptance(engine)


def test_local_engine():
    """Local engine used to acceptance test."""
    with tempfile.TemporaryDirectory() as tmpdirname:
        tmp_path = Path(tmpdirname)
        engine = EngineLocal(tmp_path)
        run_acceptance(engine)


def run_acceptance(engine: EngineABC) -> None:
    """User story for an end-to-end test."""
    s3_manager = s3.FileManager(
        engine=engine,
        transformation_list=[
            TransformationCodecs(),
            TransformationJson(),
        ],
        key_mapping=KeyMappingNumeratedFile("json"),
    )

    assert len(s3_manager) == 0

    test_content = dict(name="file-storehouse-s3", foo="bar")

    product_mapping = {id: test_content for id in range(10)}

    for id, content in product_mapping.items():
        s3_manager[id] = content

    assert len(s3_manager) == 10

    assert s3_manager == product_mapping

    for key, item in s3_manager.items():
        assert key in s3_manager
        assert isinstance(key, int)
        assert isinstance(item, dict)

    assert 10 not in s3_manager

    s3_manager[10] = dict(name="file-storehouse-s3", message="I'm new")

    assert 10 in s3_manager

    assert s3_manager != product_mapping

    del s3_manager[10]

    assert len(s3_manager) == 10

    assert s3_manager == product_mapping

    s3_manager.clear()

    assert len(s3_manager) == 0
