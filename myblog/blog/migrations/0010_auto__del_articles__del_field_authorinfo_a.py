# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Articles'
        db.delete_table('blog_articles')

        # Deleting field 'AuthorInfo.a'
        db.delete_column('blog_authorinfo', 'a')


    def backwards(self, orm):
        # Adding model 'Articles'
        db.create_table('blog_articles', (
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Category'])),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.AuthorInfo'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('h1', self.gf('django.db.models.fields.CharField')(max_length=100, unique=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('content_html', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('count', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('blog', ['Articles'])

        # Adding field 'AuthorInfo.a'
        db.add_column('blog_authorinfo', 'a',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)


    models = {
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