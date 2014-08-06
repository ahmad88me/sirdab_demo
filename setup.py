# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import sirdab_demo
version = sirdab_demo.__version__

setup(
    name='sirdab_demo',
    version=version,
    author='',
    author_email='burhan.khalid@gmail.com',
    packages=[
        'sirdab_demo',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['sirdab_demo/manage.py'],
)