#!/usr/bin/env python
import sys

if 'develop' in sys.argv:
    # use setuptools for develop, but nothing else
    from setuptools import setup
else:
    from distutils.core import setup

with open('README.rst') as file:
    long_description = file.read()

setup(name='milkywayplots',
      version='0.1',
      description='Face-on Galaxy plotting Tool',
      long_description=long_description,
      author='Adam Ginsburg',
      author_email='adam.g.ginsburg@gmail.com',
      url='http://github.com/keflavich/milkywayplots/',
      packages=['milkywayplots'],
      )
