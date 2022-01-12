#!/usr/bin/env python

import c9_qt_modern
from setuptools import setup

_version = c9_qt_modern.__version__

setup(name='c9_qt_modern',
      version=_version,
      packages=['c9_qt_modern'],
      description='Qt Widgets Modern User Interface',
      long_description=open('README.rst').read(),
      author='Cubit9 Technologies Ltd.',
      author_email='info@cubit9.com',
      url='https://www.github.com/cubit9/c9_qt_modern',
      license='MIT',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: User Interfaces'
      ],
      package_data={
          'c9_qt_modern': ['resources/*']
      },
      install_requires=['PySide6==6.2.2.1'])
