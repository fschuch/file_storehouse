"""User story for an end-to-end test."""

import tempfile
from pathlib import Path
from sys import platform

from pytest import mark

import file_storehouse as fs
from file_storehouse.extras import client


@mark.skipif(platform != "linux", reason="just runs on linux for now")
def test_s3_engine(docker_services):
    """S3 engine used to acceptance test."""
    s3_client = client(
        "s3",
        endpoint_url="http://localhost:9000",
        aws_access_key_id="compose-s3-key",
        aws_secret_access_key="compose-s3-secret",
    )

    engine = fs.EngineS3(
        s3_client=s3_client,
        bucket_name="file-storehouse-s3",
        prefix="products",
    )

    engine.ensure_bucket()

    run_acceptance(engine)


def test_local_engine():
    """Local engine used to acceptance test."""
    with tempfile.TemporaryDirectory() as tmpdirname:
        tmp_path = Path(tmpdirname)
        engine = fs.EngineLocal(tmp_path)
        run_acceptance(engine)


def run_acceptance(engine: fs.EngineABC) -> None:
    """User story for an end-to-end test."""
    file_manager = fs.FileManager(
        engine=engine,
        io_transformations=(
            fs.TransformationCodecs(),
            fs.TransformationJson(),
        ),
        key_mapping=fs.KeyMappingNumeratedFile("json"),
    )

    assert len(file_manager) == 0

    test_content = dict(name="file-storehouse", foo="bar")

    product_mapping = {id: test_content for id in range(10)}

    for id, content in product_mapping.items():
        file_manager[id] = content

    assert len(file_manager) == 10

    assert file_manager == product_mapping

    for key, item in file_manager.items():
        assert key in file_manager
        assert isinstance(key, int)
        assert isinstance(item, dict)

    assert 10 not in file_manager

    file_manager[10] = dict(name="file-storehouse", message="I'm new")

    assert 10 in file_manager

    assert file_manager != product_mapping

    del file_manager[10]

    assert len(file_manager) == 10

    assert file_manager == product_mapping

    file_manager.clear()

    assert len(file_manager) == 0
