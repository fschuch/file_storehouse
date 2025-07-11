# File-Storehouse

<p align="center">
<a href="https://github.com/fschuch/file_storehouse"><img src="https://raw.githubusercontent.com/fschuch/file_storehouse/refs/heads/main/docs/logo.png" alt="File Storehouse logo" width="320"></a>
</p>
<p align="center">
    <em>Manage files in bulk quantity using a friendly dict-like interface</em>
</p>

______________________________________________________________________

- QA:
  [![CI](https://github.com/fschuch/file_storehouse/actions/workflows/ci.yaml/badge.svg?branch=main)](https://github.com/fschuch/file_storehouse/actions/workflows/ci.yaml)
  [![CodeQL](https://github.com/fschuch/file_storehouse/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/fschuch/file_storehouse/actions/workflows/github-code-scanning/codeql)
  [![pre-commit.ci status](https://results.pre-commit.ci/badge/github/fschuch/file_storehouse/main.svg)](https://results.pre-commit.ci/latest/github/fschuch/file_storehouse/main)
  [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=fschuch_file_storehouse&metric=coverage)](https://sonarcloud.io/summary/new_code?id=fschuch_file_storehouse)
  [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=fschuch_file_storehouse&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=fschuch_file_storehouse)
  [![CodeFactor](https://www.codefactor.io/repository/github/fschuch/file_storehouse/badge)](https://www.codefactor.io/repository/github/fschuch/file_storehouse)

- Docs:
  [![Docs](https://github.com/fschuch/file_storehouse/actions/workflows/docs.yaml/badge.svg?branch=main)](https://docs.fschuch.com/file_storehouse)

- Meta:
  [![Wizard Template](https://img.shields.io/badge/Wizard-Template-%23447CAA)](https://github.com/fschuch/wizard-template)
  [![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
  [![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch)
  [![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
  ![GitHub License](https://img.shields.io/github/license/fschuch/file_storehouse?color=blue)
  [![EffVer Versioning](https://img.shields.io/badge/version_scheme-EffVer-0097a7)](https://jacobtomlinson.dev/effver)

______________________________________________________________________

## Overview

File-Storehouse is a lightweight Python package that aims to facilitate the management of files in bulk quantity.

There are four key points that are combined to achieving such a goal:

- Mapping Interface - The file managers are leveraged by the Mapping and MutableMapping interfaces, which means that everything can be done using a friendly dict-like interface. For instance:

  ```python
  # Store data to a file:
  file_manager[id] = file_content
  # Retrine data from a file
  file_content = file_manager[id]
  # Delete a file
  del file_manager[id]
  # Loop through all files
  for id, content in file_manager.items():
      pass
  # and many more...
  ```

- Engine - Choose the engine (or back-end) your file managers are connected to:

  - S3 buckets, powered by [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html);
  - Local filesystem and more are planned.

- Key Mapping - Customize a two-way key mapping between the dict-like keys and the files' location at the engines according to the business rules of your application.

- Transformations - Configure a chained operation to convert the files back and forward between your Python code and the storage. The supported operations are:

  - Encode/decode bytes and strings;
  - Dump/load Json files;
  - Compress/decompress tarballs and more transformations are planned.

## Example

Please, take a look at the [user story](tests/test_user_story.py) used for testing.

## Copyright and License

© 2022 Felipe N. Schuch.
All content is under [MIT License](https://github.com/fschuch/file_storehouse/blob/master/LICENSE).
