# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Track'
        db.create_table(u'tutorial_solved_track', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('number', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('cd', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tracks', to=orm['tutorial_solved.CD'])),
        ))
        db.send_create_signal(u'tutorial_solved', ['Track'])


    def backwards(self, orm):
        # Deleting model 'Track'
        db.delete_table(u'tutorial_solved_track')


    models = {
        u'tutorial_solved.cd': {
            'Meta': {'object_name': 'CD'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'tutorial_solved.track': {
            'Meta': {'object_name': 'Track'},
            'cd': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tracks'", 'to': u"orm['tutorial_solved.CD']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'number': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['tutorial_solved']