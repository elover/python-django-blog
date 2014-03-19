# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AuthorInfo'
        db.create_table('blog_authorinfo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=20)),
            ('icon', self.gf('django.db.models.fields.CharField')(default='', max_length=200)),
        ))
        db.send_create_signal('blog', ['AuthorInfo'])


        # Renaming column for 'Articles.author' to match new field type.
        db.rename_column('blog_articles', 'author', 'author_id')
        # Changing field 'Articles.author'
        db.alter_column('blog_articles', 'author_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.AuthorInfo']))
        # Adding index on 'Articles', fields ['author']
        db.create_index('blog_articles', ['author_id'])


    def backwards(self, orm):
        # Removing index on 'Articles', fields ['author']
        db.delete_index('blog_articles', ['author_id'])

        # Deleting model 'AuthorInfo'
        db.delete_table('blog_authorinfo')


        # Renaming column for 'Articles.author' to match new field type.
        db.rename_column('blog_articles', 'author_id', 'author')
        # Changing field 'Articles.author'
        db.alter_column('blog_articles', 'author', self.gf('django.db.models.fields.CharField')(max_length=20))

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
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['blog']