# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Category.slug'
        db.alter_column('blog_category', 'slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50))
        # Adding index on 'Category', fields ['slug']
        db.create_index('blog_category', ['slug'])


    def backwards(self, orm):
        # Removing index on 'Category', fields ['slug']
        db.delete_index('blog_category', ['slug'])


        # Changing field 'Category.slug'
        db.alter_column('blog_category', 'slug', self.gf('django.db.models.fields.CharField')(max_length=50, unique=True))

    models = {
        'blog.articles': {
            'Meta': {'ordering': "['-pub_date']", 'object_name': 'Articles'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.AuthorInfo']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.Category']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'content_html': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'count': ('django.db.models.fields.IntegerField', [], {}),
            'h1': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        'blog.authorinfo': {
            'Meta': {'object_name': 'AuthorInfo'},
            'icon': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '20'})
        },
        'blog.category': {
            'Meta': {'ordering': "['id']", 'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['blog']