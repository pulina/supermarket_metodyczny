# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Forma.wiek_min'
        db.add_column(u'base_forma', 'wiek_min',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Forma.wiek_max'
        db.add_column(u'base_forma', 'wiek_max',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'Pomysl.wiek_min'
        db.delete_column(u'base_pomysl', 'wiek_min')

        # Deleting field 'Pomysl.wiek_max'
        db.delete_column(u'base_pomysl', 'wiek_max')


    def backwards(self, orm):
        # Deleting field 'Forma.wiek_min'
        db.delete_column(u'base_forma', 'wiek_min')

        # Deleting field 'Forma.wiek_max'
        db.delete_column(u'base_forma', 'wiek_max')


        # User chose to not deal with backwards NULL issues for 'Pomysl.wiek_min'
        raise RuntimeError("Cannot reverse this migration. 'Pomysl.wiek_min' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Pomysl.wiek_min'
        db.add_column(u'base_pomysl', 'wiek_min',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Pomysl.wiek_max'
        raise RuntimeError("Cannot reverse this migration. 'Pomysl.wiek_max' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Pomysl.wiek_max'
        db.add_column(u'base_pomysl', 'wiek_max',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'base.blad': {
            'Meta': {'object_name': 'Blad'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nazwa': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'opis': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'szkodliwosc': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'base.forma': {
            'Meta': {'object_name': 'Forma'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nazwa': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'wiek_max': ('django.db.models.fields.IntegerField', [], {}),
            'wiek_min': ('django.db.models.fields.IntegerField', [], {})
        },
        u'base.komentarz': {
            'Meta': {'object_name': 'Komentarz'},
            'autor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'data_publikacji': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ocena': ('django.db.models.fields.IntegerField', [], {}),
            'pomysl': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.Pomysl']"}),
            'zawartosc': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'base.pomysl': {
            'Meta': {'object_name': 'Pomysl'},
            'blady': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['base.Blad']", 'symmetrical': 'False'}),
            'forma': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['base.Forma']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nazwa': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'opis': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'skutecznosc_base': ('django.db.models.fields.IntegerField', [], {}),
            'zaakceptowany': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'zgodnosc_z_metoda': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        u'base.tradycja': {
            'Meta': {'object_name': 'Tradycja'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nazwa': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'opis': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pomysly': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['base.Pomysl']", 'symmetrical': 'False'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['base']