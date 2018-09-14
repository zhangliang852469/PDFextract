#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from django import forms

class  PdfUpoadForm(forms.Form):
    file = forms.FileField(label='上传PDF文件')
    page = forms.IntegerField(min_value=1, label='输入提取页码')
