#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author: xuzhao
@Email: mailto:twtyjvkg@outlook.com
@File: setup.py
@Description: 
@Time: 2018/7/24 22:07
"""
from distutils.core import setup

import setuptools

with open('README.md', 'r', encoding='utf8') as fh:
    long_description = fh.read()

setup(name='magic-django-markdown-editor',
      version='1.0',
      description='为django量身定制的markdown编辑器',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='xuzhao',
      author_email='twtyjvkg@outlook.com',
      url='https://markdown.xuzhao.xin',
      keywords='django markdown editor base on editormd',
      packages=setuptools.find_packages(),
      zip_safe=False,
      include_package_data=True,
      classifiers=(
          "Programming Language :: Python",
          "Development Status :: 4 - Beta",
          "Operating System :: OS Independent",
          "License :: OSI Approved :: Apache Software License",
          "Framework :: Django"
      ),
      )