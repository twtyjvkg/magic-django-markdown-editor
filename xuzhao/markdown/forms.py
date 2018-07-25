#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author: xuzhao
@Email: mailto:twtyjvkg@outlook.com
@File: forms.py
@Description: 表单
@Time: 2018/7/24 21:30
"""
from django import forms

from .widgets import MarkdownWidget, AdminMarkdownWidget


class MarkdownField(forms.CharField):
    widget = MarkdownWidget


class AdminMarkdownField(forms.CharField):
    widget = AdminMarkdownWidget