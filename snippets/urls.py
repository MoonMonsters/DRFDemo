#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: _Tao
# @Time: 19-3-3 19:46
from django.urls import path, include, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from snippets import views, views_v2, views_v3
from snippets.views_v3 import SnippetViewSet, UserViewSet, api_root

router = DefaultRouter()
router.register('snippets', SnippetViewSet)
router.register('users', UserViewSet)

schema_view = get_schema_view(title='PasterBin Api')

snippet_list = SnippetViewSet.as_view(
	{
		'get': 'list',
		'post': 'create'
	}
)

snippet_detail = SnippetViewSet.as_view(
	{
		'get': 'retrive',
		'put': 'update',
		'patch': 'partial_update',
		'delete': 'destroy',
	}
)

snippet_highlight = SnippetViewSet.as_view(
	{
		'get', 'highlight',
	}, renderer_classes=[renderers.StaticHTMLRenderer]
)

user_list = UserViewSet.as_view(
	{
		'get': 'list'
	}
)

user_detail = UserViewSet.as_view(
	{
		'get': 'retrieve'
	}
)

app_name = 'snippets'
# urlpatterns = [
# 	path('', views_v3.api_root),
# 	path('snippets/', views_v3.SnippetList2.as_view(), name='snippet-list'),
# 	re_path('snippet/(?P<pk>[0-9]+)/', views_v3.SnippetDetail2.as_view(), name='snippet-detail'),
# 	path('users/', views_v3.UserList.as_view(), name='user-list'),
# 	re_path('users/(?P<pk>[0-9]+)/', views_v3.UserDetail.as_view(), name='user-detail'),
# 	re_path('snippets/(?P<pk>[0-9]+)/highlights/', views_v3.SnippetHighlight.as_view(), name='snippet-highlight'),
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns = format_suffix_patterns([
	path('schema/', schema_view),
	path('', api_root),
	path('snippets/', snippet_list, name='snippet-list'),
	path('snippets/(?P<pk>[0-9]+)/', snippet_detail, name='snippet-detail'),
	path('snippets/(?P<pk>[0-9]+)/highlight/', snippet_highlight, name='snippet-highlight'),
	path('users/', user_list, name='user-list'),
	path('users/(?P<pk>[0-9]+)/', user_detail, name='user-detail')
])
