# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'A'
        db.create_table('blog_a', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('n', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('blog', ['A'])


        # Changing field 'Articles.h1'
        db.alter_column('blog_articles', 'h1', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100))

        # Changing field 'AuthorInfo.name'
        db.alter_column('blog_authorinfo', 'name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100))

        # Changing field 'AuthorInfo.icon'
        db.alter_column('blog_authorinfo', 'icon', self.gf('django.db.models.fields.CharField')(max_length=100))

        # Changing field 'Category.slug'
        db.alter_column('blog_category', 'slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=100))

        # Changing field 'Category.name'
        db.alter_column('blog_category', 'name', self.gf('django.db.models.fields.CharField')(max_length=100))

    def backwards(self, orm):
        # Deleting model 'A'
        db.delete_table('blog_a')


        # Changing field 'Articles.h1'
        db.alter_column('blog_articles', 'h1', self.gf('django.db.models.fields.CharField')(max_length=50, unique=True))

        # Changing field 'AuthorInfo.name'
        db.alter_column('blog_authorinfo', 'name', self.gf('django.db.models.fields.CharField')(max_length=20, unique=True))

        # Changing field 'AuthorInfo.icon'
        db.alter_column('blog_authorinfo', 'icon', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Category.slug'
        db.alter_column('blog_category', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True))

        # Changing field 'Category.name'
        db.alter_column('blog_category', 'name', self.gf('django.db.models.fields.CharField')(max_length=20))

    models = {
        'blog.a': {
            'Meta': {'object_name': 'A'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'n': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'blog.articles': {
            'Meta': {'ordering': "['-pub_date']", 'object_name': 'Articles'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.AuthorInfo']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.Category']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'content_html': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'count': ('django.db.models.fields.IntegerField', [], {}),
            'h1': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        'blog.authorinfo': {
            'Meta': {'object_name': 'AuthorInfo'},
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'blog.category': {
            'Meta': {'ordering': "['id']", 'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['blog']