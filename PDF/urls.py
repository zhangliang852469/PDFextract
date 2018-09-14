#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from django.urls import path

from . import views

# 命名空间
app_name = 'PDF'

urlpatterns = [
    # 上传pdf文件后，用户需要输入提取的页面，返回需要提取的页面
    path('extract/', views.pdf_extract, name='pdf_extract')
]




