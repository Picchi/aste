# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        orm.CD.objects.create(name="Rock Music", description="It rocks!!")
        orm.CD.objects.create(name="Relax Music", description="Relax yourself...")
        orm.CD.objects.create(name="Classic Music", description="For Mozart estimators")
	orm.CD.objects.create(name="Pop Music", description="Pure pop!")

    def backwards(self, orm):
        orm.CD.objects.all().delete()

    models = {
        u'tutorial_solved.cd': {
            'Meta': {'object_name': 'CD'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['tutorial_solved']
    symmetrical = True
