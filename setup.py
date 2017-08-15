import codecs
import os
import re

from setuptools import setup


# read version in __init__.py
# code adapted from: https://github.com/pypa/pip/blob/1.5.6/setup.py#L33
here = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    return codecs.open(os.path.join(here, *parts), 'r').read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)

    raise RuntimeError("Unable to find version string.")


setup(name='optimization_test',
      version=find_version("optimization_test/__init__.py"),
      description='A simple Python library provides numerous test functions for optimization algorithms.',
      url='http://github.com/ngroup/optimization_test',
      author='Chun Nien',
      author_email='contact@chunnien.com',
      license='MIT',
      packages=['optimization_test'],
      zip_safe=False,
      install_requires=[
          'numpy',]
      )
