# File-Storehouse

[![Test and build](https://github.com/fschuch/file_storehouse/actions/workflows/ci.yml/badge.svg)](https://github.com/fschuch/file_storehouse/actions/workflows/ci.yml)
![python](https://img.shields.io/badge/Python-3.8%2B-brightgreen)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PyPI Version](https://img.shields.io/pypi/v/file_storehouse.svg)](https://pypi.org/project/file_storehouse/)

## Main Features

File-Storehouse is a lightweight Python package that aims to facilitate the management of files in bulk quantity.

There are four key points that are combined to achieving such a goal:

* Mapping Interface - The file managers are leveraged by the Mapping and MutableMapping interfaces, which means that everything can be done using a friendly dict-like interface. For instance:

  ```python
  # Store data to a file:
  file_manager[id] = file_content
  # Retrine data from a file
  file_content = file_manager[<id>]
  # Delete a file
  del file_manager[id]
  # Loop through all files
  for id, content in file_manager.items():
      pass
  # and many more...
  ```

* Engine - Choose the engine (or back-end) your file managers are connected to:

  * S3 buckets, powered by [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html);
  * Local filesystem and more are planned.

* Key Mapping - Customize a two-way key mapping between the dict-like keys and the files' location at the engines according to the business rules of your application.

* Transformations - Configure a chained operation the convert the files back and forward between your Python code and the storage. The supported operations are:

  * Encode/decode bytes and strings;
  * Dump/load Json files;
  * Compress/decompress tarballs and more transformations are planned.

## Example

Please, take a look at the [user story](tests/test_user_story.py) used for testing.

## Copyright and License

© 2022 Felipe N. Schuch. All content is under [MIT License](https://github.com/fschuch/file_storehouse/blob/master/LICENSE).
