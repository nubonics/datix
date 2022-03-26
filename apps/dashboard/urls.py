# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.dashboard import views

urlpatterns = [

    # The dashboard page
    path('', views.index, name='dashboard'),

    # Matches any html file
    re_path("" + r'^.*\.*', views.pages, name='pages'),

]
