#! -*- coding:utf-8 -*-

from setuptools import setup, find_packages
import glob

# get version data
with open("VERSION") as fo:
    version = fo.read()

setup(
     name='mikado-core',
     version=version,
     description='Core files for Mikado Software OSS projects',
     author='author',
     packages=find_packages(exclude=('tests')),
     # Any scripts (i.e. python/bash) found here will be added to PATH
     scripts=glob.glob('scripts/*')
)
