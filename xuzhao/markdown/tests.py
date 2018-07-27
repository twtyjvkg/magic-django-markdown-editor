#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author: xuzhao
@Email: mailto:twtyjvkg@outlook.com
@File: tests.py
@Description: 
@Time: 2018/7/27 16:49
"""
from django import forms
from django.test import TestCase
from xuzhao.markdown.widgets import AdminMarkdownWidget, MarkdownWidget


class AdminMarkdownFieldTest(TestCase):

    class ArticleForm(forms.ModelForm):
        body = forms.CharField(widget=AdminMarkdownWidget())


class MarkdownFieldTest(TestCase):
    class ArticleForm(forms.ModelForm):
        body = forms.CharField(widget=MarkdownWidget())