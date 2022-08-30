"""Test the bucket manager."""

from io import StringIO

import pytest

from file_storehouse import EngineS3, FileManagerReadOnly
from file_storehouse.extras import Stubber, client


@pytest.fixture(scope="module")
def s3_client():
    """Test fixture containing a S3 client."""
    return client("s3")


class TestS3ManagerReadOnly:
    """Test the read only manager based on the Mapping interface."""

    @pytest.fixture(scope="class")
    def s3_engine(self, s3_client):
        """Test fixture containing a S3 engine."""
        return EngineS3(s3_client=s3_client, bucket_name="test-bucket")

    @pytest.fixture(scope="class")
    def manager(self, s3_engine):
        """Test fixture that returns the read only manager."""
        return FileManagerReadOnly(s3_engine)

    def test_getitem__success(self, manager):
        """Test if the get item syntax works."""
        s3_key = "test.txt"
        desired_content = "some text for testing"

        with Stubber(manager.engine.s3_client) as stubber:
            stubber.add_response(
                method="get_object",
                service_response=dict(Body=StringIO(desired_content)),
                expected_params=dict(Bucket="test-bucket", Key=s3_key),
            )
            actual_content = manager[s3_key]

        assert actual_content == desired_content
        stubber.assert_no_pending_responses()

    def test_getitem__error_no_such_key(self, manager):
        """Test if the get item syntax raises key error if the object is not found."""
        s3_key = "test.txt"

        with Stubber(manager.engine.s3_client) as stubber:
            stubber.add_client_error(
                method="get_object",
                service_error_code="NoSuchKey",
                expected_params=dict(Bucket="test-bucket", Key=s3_key),
            )
            with pytest.raises(KeyError, match=f"No such key='{s3_key}'"):
                manager[s3_key]

    @pytest.mark.parametrize("method", ["__setitem__", "__delitem__", "pop", "clear"])
    def test_writing_methods_are_not_found(self, manager, method):
        """Double-check if the writing methods for MutableMapping are not found."""
        assert hasattr(manager, method) is False
