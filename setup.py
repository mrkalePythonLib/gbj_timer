#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Setup function for the package."""

from setuptools import setup

setup(
  name='gbj_timer',
  version='1.0.0',
  description='Python package for module timer.',
  long_description='Module for managing timers.',
  classifiers=[
    'Development Status :: 4 - Beta',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.8',
    'Topic :: System :: Monitoring',
  ],
  keywords='timer',
  url='http://github.com/mrkalePythonLib/gbj_timer',
  author='Libor Gabaj',
  author_email='libor.gabaj@gmail.com',
  license='MIT',
  packages=['gbj_timer'],
  install_requires=[],
  include_package_data=True,
  zip_safe=False
)
