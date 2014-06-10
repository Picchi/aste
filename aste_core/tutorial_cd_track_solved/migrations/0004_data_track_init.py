# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models


class Migration(DataMigration):

    def forwards(self, orm):

        import random
        for cd in orm.CD.objects.all():
            for n in range(1, random.randint(3, 6)):
                orm.Track.objects.create(number=n, name="Track "+str(n), cd=cd)

    def backwards(self, orm):
        orm.Track.objects.all().delete()

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
    symmetrical = True
