#-*- coding:utf-8 -*-
__author__ = 'mac'
from django.contrib import admin
from blog.models import *


# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     extra = 3
#
#
# class PollAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ("问题", {'fields': ['question']}),
#         ("时间信息", {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     inlines = [ChoiceInline]
#
#
# admin.site.register(Poll, PollAdmin)
# admin.site.register(Choice)
admin.site.register(AuthorInfo)
admin.site.register(Articles)
admin.site.register(Category)

