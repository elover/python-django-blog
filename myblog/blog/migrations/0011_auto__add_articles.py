# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Articles'
        db.create_table('blog_articles', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('h1', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('content_html', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('count', self.gf('django.db.models.fields.IntegerField')()),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.AuthorInfo'])),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Category'])),
        ))
        db.send_create_signal('blog', ['Articles'])


    def backwards(self, orm):
        # Deleting model 'Articles'
        db.delete_table('blog_articles')


    models = {
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