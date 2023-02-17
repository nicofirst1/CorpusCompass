#!/usr/bin/env python

from distutils.core import setup

setup(name='CorpusCompass',
      version='2.0',
      description='Utilities tool for linguistic annotation',
      author="Nicolo' Brandizzi",
      author_email='brandizzi@diag.uniroma1.it',
      url='https://github.com/nicofirst1/CorpusCompass',
      install_requires=['nltk', "pandas", "matplotlib", "numpy", "PySide6"],
      )
