"""Test the options available for the two-way mapping."""

from pathlib import Path

from hypothesis import given
from hypothesis import strategies as st
from pytest import fixture

from file_storehouse.key_mapping import (
    KeyMappingNumeratedFile,
    KeyMappingNumeratedFolder,
    KeyMappingRaw,
)


class TestKeyMappingRaw:
    """Test the raw key mapping."""

    @fixture(scope="class")
    def mapping(self):
        """Test fixture to build a raw key mapping."""
        return KeyMappingRaw()

    @given(s3_key=st.text())
    def test_get_dict_key_from_engine_and_then_back(self, mapping, s3_key):
        """Test the key mapping."""
        dict_key = mapping.get_dict_key_from_engine(s3_key)
        assert s3_key == mapping.get_engine_key_from_dict(dict_key)

    @given(dict_key=st.text())
    def test_get_engine_key_from_dict_and_then_back(self, mapping, dict_key):
        """Test the key mapping."""
        s3_key = mapping.get_engine_key_from_dict(dict_key)
        assert dict_key == mapping.get_dict_key_from_engine(s3_key)


class TestKeyMappingNumeratedFile:
    """Test the numerated file key mapping."""

    @fixture(scope="class")
    def mapping(self):
        """Test fixture to build a numerated key mapping."""
        return KeyMappingNumeratedFile("json")

    @given(number=st.integers())
    def test_get_dict_key_from_engine_and_then_back(self, mapping, number):
        """Test the key mapping."""
        engine_key = Path(f"{number}.json")
        dict_key = mapping.get_dict_key_from_engine(engine_key)
        assert engine_key == mapping.get_engine_key_from_dict(dict_key)

    @given(dict_key=st.integers())
    def test_get_engine_key_from_dict_and_then_back(self, mapping, dict_key):
        """Test the key mapping."""
        engine_key = mapping.get_engine_key_from_dict(dict_key)
        assert dict_key == mapping.get_dict_key_from_engine(engine_key)


class TestKeyMappingNumeratedFolder:
    """Test the numerated folder key mapping."""

    @fixture(scope="class")
    def mapping(self):
        """Test fixture to build a numerated key mapping."""
        return KeyMappingNumeratedFolder("test.json")

    @given(number=st.integers())
    def test_get_dict_key_from_engine_and_then_back(self, mapping, number):
        """Test the key mapping."""
        engine_key = Path(f"{number}/test.json")
        dict_key = mapping.get_dict_key_from_engine(engine_key)
        assert engine_key == mapping.get_engine_key_from_dict(dict_key)

    @given(dict_key=st.integers())
    def test_get_engine_key_from_dict_and_then_back(self, mapping, dict_key):
        """Test the key mapping."""
        engine_key = mapping.get_engine_key_from_dict(dict_key)
        assert dict_key == mapping.get_dict_key_from_engine(engine_key)
