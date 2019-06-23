import os
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

# list of (destination, source_file) tuples
DATA_FILES = [('~/.local/bin', ['m7i92/mesaflash64', 'm7i92/mesaflash32',])]
data_files = [(os.path.expanduser(dest), src_list) for dest, src_list in DATA_FILES]

setup(
    name="7i92",
    version="0.1",
    author="John Thornton",
    author_email="<jt@gnipsel.com>",
    description="Mesa configuration tool for 7i92",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jethornton/7i92",
    download_url="https://github.com/jethornton/7i92/tarball/master",
    python_requires='>=3',
    packages=find_packages(),
    data_files=data_files,
    include_package_data=True,
    entry_points={
        'gui_scripts': ['7i92=m7i92.7i92:main',],
    },
)

