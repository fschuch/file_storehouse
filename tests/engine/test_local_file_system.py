"""Test the local file system."""

from pathlib import Path

import pytest

from file_storehouse.engine.local_file_system import EngineLocal


@pytest.fixture
def local_engine(tmp_path):
    """Fixture to provide the engine."""
    yield EngineLocal(base_path=tmp_path)


@pytest.fixture
def dummy_nested_folders(local_engine):
    """Fixture to create a nested folder structure."""
    test_path = Path(local_engine.base_path)
    for i in range(4):
        test_path /= str(i)
    test_path.mkdir(parents=True)
    return test_path


@pytest.fixture(scope="module")
def filename():
    """Fixture with a dummy filename."""
    return "test_file.txt"


@pytest.fixture(scope="module")
def file_content():
    """Fixture with a dummy file content."""
    return b"testing file"


@pytest.fixture
def file_path(local_engine, file_content, filename):
    """Fixture that creates the dummy file and returns its path."""
    file_path = local_engine.base_path / filename
    file_path.write_bytes(file_content)
    return file_path


class TestEngineLocal:
    """Test the engine to manage the local file system."""

    def test_get_item_success(self, local_engine, file_content, file_path):
        """Test get item."""
        assert local_engine.get_item(file_path) == file_content

    def test_get_item_fail_no_such_key(self, local_engine):
        """Test that KeyError is raised when the file is not found."""
        filename = "test_file.txt"
        file_path = local_engine.base_path / filename

        with pytest.raises(KeyError):
            local_engine.get_item(file_path)

    def test_set_item(self, local_engine, file_path, file_content):
        """Test set item."""
        local_engine.set_item(file_path, file_content)

        assert file_path.read_bytes() == file_content

    def test_remove_empty_folders_initial_length(
        self, local_engine, dummy_nested_folders
    ):
        """Test the initial length of the nested folders fixture."""
        assert len(list(local_engine.base_path.rglob("*"))) == 4

    def test_remove_empty_folders_do_not_work_if_folder_is_not_empty(
        self,
        local_engine,
        dummy_nested_folders,
    ):
        """Test that the engine can not remove a folder that when that are files."""
        filename = "test_file.txt"
        file_content = b"testing file"
        file_path = dummy_nested_folders / filename

        file_path.write_bytes(file_content)

        local_engine._remove_empty_folders(dummy_nested_folders)

        assert len(list(local_engine.base_path.rglob("*"))) == 5

    def test_remove_empty_folders_empty(
        self,
        local_engine,
        dummy_nested_folders,
    ):
        """Test that the engine delete empty nested folders when they are all empty."""
        local_engine._remove_empty_folders(dummy_nested_folders)

        assert len(list(local_engine.base_path.rglob("*"))) == 0

    def test_delete_item(self, local_engine, file_path):
        """Test delete item."""
        assert file_path.is_file()
        local_engine.delete_item(file_path)
        assert not file_path.is_file()

    def test_convert_to_absolute_path(self, local_engine, filename, file_path):
        """Test convert the path from relative to absolute."""
        absolute_path = local_engine.convert_to_absolute_path(filename)
        assert absolute_path == file_path

    def test_convert_to_relative_path(self, local_engine, filename, file_path):
        """Test convert the path from absolute to relative."""
        relative_path = local_engine.convert_to_relative_path(file_path)
        assert relative_path == Path(filename)
