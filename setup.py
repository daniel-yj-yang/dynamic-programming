# -*- coding: utf-8 -*-

#  Author: Daniel Yang <daniel.yj.yang@gmail.com>
#
#  License: BSD-3-Clause

import setuptools

import DP

with open("README.rst", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as fh:
    required = fh.read().splitlines()

setuptools.setup(
    name="dynamic-programming",
    version=DP.__version__,
    license=DP.__license__,
    author="Daniel Yang",
    author_email="daniel.yj.yang@gmail.com",
    description="Library for Studying Dynamic Programming",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/daniel-yj-yang/dynamic-programming",
    packages=setuptools.find_packages(),
    # https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    install_requires=required,
    python_requires='>=3.8',
    include_package_data=True,
)
