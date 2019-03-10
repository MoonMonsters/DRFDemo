#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: _Tao
# @Time: 19-3-10 13:40


from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

	def has_object_permission(self, request, view, obj):
		"""
		判断登录用户是否有某种权限
		:param request: 请求对象
		:param view:
		:param obj: 绑定的ModelSerializer对象
		:return: 是否有权限
		"""
		if request.method in permissions.SAFE_METHODS:
			return True

		return obj.owner == request.user
