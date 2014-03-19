#-*- coding:utf-8 -*-
#url 规则
import sys
from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
# from blog import views

urlpatterns = patterns('',
                       url(r'^$', 'blog.views.index', name='index'),
                       url(r'^category/(?P<slug>[^/]+)/$', 'blog.views.category', name='category'),
                       # url(r'^$', ListView.as_view(
                       #     queryset=Poll.objects.order_by('-pub_date')[:5],
                       #     context_object_name='latest_poll_list',
                       #     template_name='mainTem/index.html'),
                       #     name='index'),^blog\/([\%\w\d]+)\/$
                       url(r'^blog\/(?P<article_id>\d+)/$', 'blog.views.article', name="article"),
                       url(r'^list$', 'blog.views.list', name="list"),
                       url(r'^info$', 'blog.views.info', name="info"),
                       url(r'^music\/(?P<article_id>\d+)/$', 'blog.views.music', name="music"),
                       url(r'^postArticle/$', 'blog.views.postArticle', name="postArticle"),
                       url(r'^invite/$', 'blog.views.invite', name="invite"),
                       url(r'^changeLog/$', 'blog.views.changeLog', name="changeLog")

)

