from setuptools import setup
import re
import os
from os import path

_version_re = re.compile(r"(?<=^__version__ = (\"|'))(.+)(?=\"|')")

def get_version(rel_path: str) -> str:
    """
    Searches for the ``__version__ = `` line in a source code file.

    https://packaging.python.org/en/latest/guides/single-sourcing-package-version/
    """
    with open(rel_path, 'r') as f:
        matches = map(_version_re.search, f)
        filtered = filter(lambda m: m is not None, matches)
        version = next(filtered, None)
        if version is None:
            raise RuntimeError(f'Could not find __version__ in {rel_path}')
        return version.group(0)

with open(path.join(path.dirname(path.abspath(__file__)), 'README.rst')) as f:
    readme = f.read()

setup(
    name                = 'pipeline2cube',
    version             = get_version('pipeline2cube/pipeline2cube.py'),
    description         = 'A ChRIS helper app that registers pipelines to a CUBE instance',
    long_description    =  readme,
    author              = 'FNNDSC',
    author_email        = 'rudolph.pienaar@childrens.harvard.edu',
    url                 = 'https://github.com/FNNDSC/plugin2cube',
    # py_modules          = ['plugin2cube'],
    install_requires    = ['pudb', 'loguru', 'python-chrisclient', 'plugin2cube'],
    packages            = ['pipeline2cube'],
    license             = 'MIT',
    entry_points        = {
        'console_scripts': [
            'pipeline2cube = pipeline2cube.__main__:main'
        ]
    },
    classifiers         =[
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.'
    ],
    extras_require      ={
        'none': [],
        'dev': [
            'pytest~=7.1',
            'pytest-mock~=3.8'
        ]
    }
)