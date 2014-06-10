# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        for cd in orm.CD.objects.all():
            cd.description = "Questo CD contiene " + str(cd.tracks.count()) + " tracce"
            cd.save()
        

    def backwards(self, orm):
        for cd in orm.CD.objects.all():
            cd.description = "Descrizione di default"
            cd.save()
        #pass

    models = {
        u'tutorial_solved.cd': {
            'Meta': {'object_name': 'CD'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
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
    symmetrical = True
