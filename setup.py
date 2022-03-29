#!/usr/bin/env python

import os
import glob

from setuptools import find_packages

from numpy.distutils.core import Extension, setup


# Top-level setup
setup(
    name="eco_case_studies",
    version="0.0.1",
    description="Case studies for ECO",
    url="https://github.com/dakotaramos/eco_case_studies",
    author="NREL ECO Team",
    author_email="dakota.potereramos@nrel.gov",
    install_requires=[],
    python_requires=">=3.7",
    package_data={},
    # package_dir      = {'': 'wisdem'},
    packages=find_packages(exclude=["docs", "tests", "ext"]),
    entry_points={},
)