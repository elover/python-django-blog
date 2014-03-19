# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Music'
        db.delete_table('blog_music')

        # Adding field 'Articles.music_url'
        db.add_column('blog_articles', 'music_url',
                      self.gf('django.db.models.fields.TextField')(default='\xe8\xaf\xb7\xe6\x8f\x90\xe9\x86\x92\xe6\x88\x91\xef\xbc\x8c\xe9\x9f\xb3\xe4\xb9\x90\xe6\x94\xbe\xe4\xb8\x8d\xe4\xba\x86\xe4\xba\x86'),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Music'
        db.create_table('blog_music', (
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100, unique=True)),
        ))
        db.send_create_signal('blog', ['Music'])

        # Deleting field 'Articles.music_url'
        db.delete_column('blog_articles', 'music_url')


    models = {
        'blog.articles': {
            'Meta': {'ordering': "['-pub_date']", 'object_name': 'Articles'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.AuthorInfo']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.Category']"}),
            'content': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'content_html': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'h1': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'music_url': ('django.db.models.fields.TextField', [], {'default': "'\\xe8\\xaf\\xb7\\xe6\\x8f\\x90\\xe9\\x86\\x92\\xe6\\x88\\x91\\xef\\xbc\\x8c\\xe9\\x9f\\xb3\\xe4\\xb9\\x90\\xe6\\x94\\xbe\\xe4\\xb8\\x8d\\xe4\\xba\\x86\\xe4\\xba\\x86'"}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': "''"})
        },
        'blog.authorinfo': {
            'Meta': {'object_name': 'AuthorInfo'},
            'icon': ('django.db.models.fields.CharField', [], {'default': "'/static/images/default.jpg'", 'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'nan'", 'unique': 'True', 'max_length': '100'})
        },
        'blog.category': {
            'Meta': {'ordering': "['id']", 'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'unique': 'True', 'max_length': '100'})
        }
    }

    complete_apps = ['blog']