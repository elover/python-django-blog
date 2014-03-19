#-*- coding:utf-8 -*-
import datetime
from django.utils import timezone
from django.db import models
from markdown import markdown
from datetime import date

# Create your models here.


class Category(models.Model):
#  分类表
    name = models.CharField(max_length=100, default='')
    slug = models.SlugField(max_length=100, default='', unique=True, verbose_name=u'Slug')

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return 'category', None, {'slug': self.slug}

    class Meta:
        ordering = ['id']
        verbose_name_plural = verbose_name = u'分类'


class AuthorInfo(models.Model):
    # 作者信息表
    name = models.CharField(max_length=100, default='nan', unique=True)
    icon = models.CharField(max_length=100, default='/static/images/default.jpg', )

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = verbose_name = u'作者'


class Articles(models.Model):
    h1 = models.CharField(max_length=100, default='', unique=True)
    content = models.TextField(default='')
    content_html = models.TextField(blank=True, default='', null=True)
    count = models.IntegerField(default=0, blank=True)
    music_url = models.TextField(default="", blank=True, null=True)
    author = models.ForeignKey(AuthorInfo, verbose_name=u"作者")
    pub_date = models.DateTimeField('发布日期', auto_now_add=True, editable=True)
    category = models.ForeignKey(Category, blank=True,verbose_name=u'分类')

    def __unicode__(self):
        return self.h1

    def save(self):
        self.content_html = markdown(self.content, extensions=["codehilite"])
        super(Articles, self).save()

    @models.permalink
    def get_absolute_url(self):
        return 'article', (), {'article_id': self.id}

    class Meta:
        ordering = ['-pub_date']
        verbose_name_plural = verbose_name = u'文章'




