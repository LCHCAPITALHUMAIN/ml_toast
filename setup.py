# Copyright 2022 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Setup for ml_toast package."""

import os

from setuptools import find_packages
from setuptools import setup

_CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def _get_readme():
  try:
    readme = open(
        os.path.join(_CURRENT_DIR, "README.md"), encoding="utf-8").read()
  except OSError:
    readme = ""
  return readme


def _get_version():
  with open(os.path.join(_CURRENT_DIR, "ml_toast", "__init__.py")) as fp:
    for line in fp:
      if line.startswith("__version__") and "=" in line:
        version = line[line.find("=") + 1:].strip(" '\"\n")
        if version:
          return version
    raise ValueError("`__version__` not defined in `ml_toast/__init__.py`")


def _parse_requirements(path):
  with open(os.path.join(_CURRENT_DIR, path)) as f:
    return [
        line.rstrip()
        for line in f
        if not (line.isspace() or line.startswith("#"))
    ]


_VERSION = _get_version()
_README = _get_readme()
_REQUIREMENTS = _parse_requirements(
    os.path.join(_CURRENT_DIR, "requirements.txt"))

setup(
    name="ml_toast",
    version=_VERSION,
    description="Package for multilingual topic clustering",
    long_description="\n".join([_README]),
    long_description_content_type="text/markdown",
    author="Google LLC",
    author_email="no-reply@google.com",
    license="Apache 2.0",
    packages=find_packages(),
    install_requires=_REQUIREMENTS,
    url="https://github.com/google/ml_toast",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Programming Language :: Python :: 3.9",
    ],
)
