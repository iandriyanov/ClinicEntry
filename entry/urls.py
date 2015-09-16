# -*- coding: utf-8 -*-

############################################
#
# File Name : urls.py
#
# Purpose :
#
# Creation Date : 16-09-2015
#
# Last Modified : Ср. 16 сент. 2015 08:24:40
#
# Created By : iandriyanov
#
############################################


from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
]
