"""User story for an end-to-end test."""

from sys import platform
from typing import Any

from pytest import mark

import file_storehouse as s3
from file_storehouse.engine import EngineS3
from file_storehouse.key_mapping import KeyMappingNumeratedFile
from file_storehouse.transformation import TransformationCodecs, TransformationJson


@mark.skipif(platform != "linux", reason="just runs on linux for now")
def test_acceptance(docker_services: Any) -> None:
    """
    User story for an end-to-end test.

    Parameters
    ----------
    docker_services : Any
        Test fixture used to start all services from a docker compose file.
        After test are finished, shutdown all services.

    """
    s3_client = s3.client(
        "s3",
        endpoint_url="http://localhost:9000",
        aws_access_key_id="compose-s3-key",
        aws_secret_access_key="compose-s3-secret",
    )

    s3_engine = EngineS3(
        s3_client=s3_client,
        bucket_name="file-storehouse-s3",
        prefix="products",
    )

    s3_engine.ensure_bucket()

    s3_manager = s3.FileManager(
        engine=s3_engine,
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
