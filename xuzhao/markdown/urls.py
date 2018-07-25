#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Author: xuzhao
@Email: mailto:twtyjvkg@outlook.com
@File: urls.py
@Description: 
@Time: 2018/7/24 21:36
"""
from django import VERSION

from .views import upload_image
if VERSION < (1, 9):
    from django.conf.urls import patterns, url
    urlpatterns = patterns('',
        url(r'^uploadimage/$', upload_image),
    )
else:
    from django.conf.urls import  url

    app_name = 'markdown'
    urlpatterns=[
        url(r'^uploadimage/$', upload_image),

    ]