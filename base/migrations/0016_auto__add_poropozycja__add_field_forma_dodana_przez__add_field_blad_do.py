# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Poropozycja'
        db.create_table(u'base_poropozycja', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nick', self.gf('django.db.models.fields.CharField')(default='Niewiadomo', max_length=200)),
            ('email', self.gf('django.db.models.fields.EmailField')(default='Niewiadomo', max_length=200)),
            ('stopien_instruktorski', self.gf('django.db.models.fields.CharField')(default='Niewiadomo', max_length=200)),
            ('funkcja', self.gf('django.db.models.fields.CharField')(default='Niewiadomo', max_length=200)),
            ('plec', self.gf('django.db.models.fields.CharField')(default='Niewiadomo', max_length=200)),
            ('organizacja', self.gf('django.db.models.fields.CharField')(default='Niewiadomo', max_length=200)),
            ('skad_jestes', self.gf('django.db.models.fields.CharField')(default='Niewiadomo', max_length=200)),
            ('propozycja_dotyczy', self.gf('django.db.models.fields.CharField')(default='Niewiadomo', max_length=200)),
            ('opis_problemu', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'base', ['Poropozycja'])

        # Adding field 'Forma.dodana_przez'
        db.add_column(u'base_forma', 'dodana_przez',
                      self.gf('django.db.models.fields.CharField')(default='System', max_length=200),
                      keep_default=False)

        # Adding field 'Blad.dodana_przez'
        db.add_column(u'base_blad', 'dodana_przez',
                      self.gf('django.db.models.fields.CharField')(default='System', max_length=200),
                      keep_default=False)

        # Adding field 'Pomysl.dodana_przez'
        db.add_column(u'base_pomysl', 'dodana_przez',
                      self.gf('django.db.models.fields.CharField')(default='System', max_length=200),
                      keep_default=False)

        # Adding field 'Tradycja.dodana_przez'
        db.add_column(u'base_tradycja', 'dodana_przez',
                      self.gf('django.db.models.fields.CharField')(default='System', max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Poropozycja'
        db.delete_table(u'base_poropozycja')

        # Deleting field 'Forma.dodana_przez'
        db.delete_column(u'base_forma', 'dodana_przez')

        # Deleting field 'Blad.dodana_przez'
        db.delete_column(u'base_blad', 'dodana_przez')

        # Deleting field 'Pomysl.dodana_przez'
        db.delete_column(u'base_pomysl', 'dodana_przez')

        # Deleting field 'Tradycja.dodana_przez'
        db.delete_column(u'base_tradycja', 'dodana_przez')


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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'base.blad': {
            'Meta': {'object_name': 'Blad'},
            'dodana_przez': ('django.db.models.fields.CharField', [], {'default': "'System'", 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nazwa': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'opis': ('django.db.models.fields.TextField', [], {}),
            'szkodliwosc': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'base.forma': {
            'Meta': {'object_name': 'Forma'},
            'dodana_przez': ('django.db.models.fields.CharField', [], {'default': "'System'", 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nazwa': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'opis': ('django.db.models.fields.TextField', [], {})
        },
        u'base.funkcja': {
            'Meta': {'object_name': 'Funkcja'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nazwa': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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
        u'base.okres': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'Okres'},
            'forma': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['base.Forma']", 'null': 'True', 'blank': 'True'}),
            'funkcja': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['base.Funkcja']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nazwa': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'opis': ('django.db.models.fields.TextField', [], {}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'stopien': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'wiek_max': ('django.db.models.fields.IntegerField', [], {}),
            'wiek_min': ('django.db.models.fields.IntegerField', [], {})
        },
        u'base.pomysl': {
            'Meta': {'object_name': 'Pomysl'},
            'blady': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['base.Blad']", 'null': 'True', 'blank': 'True'}),
            'dodana_przez': ('django.db.models.fields.CharField', [], {'default': "'System'", 'max_length': '200'}),
            'forma': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['base.Forma']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nazwa': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'opis': ('django.db.models.fields.TextField', [], {}),
            'skutecznosc_base': ('django.db.models.fields.IntegerField', [], {}),
            'tradycja': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['base.Tradycja']", 'null': 'True', 'blank': 'True'}),
            'zaakceptowany': ('django.db.models.fields.BooleanField', [], {}),
            'zgodnosc_z_metoda': ('django.db.models.fields.BooleanField', [], {})
        },
        u'base.poropozycja': {
            'Meta': {'object_name': 'Poropozycja'},
            'email': ('django.db.models.fields.EmailField', [], {'default': "'Niewiadomo'", 'max_length': '200'}),
            'funkcja': ('django.db.models.fields.CharField', [], {'default': "'Niewiadomo'", 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nick': ('django.db.models.fields.CharField', [], {'default': "'Niewiadomo'", 'max_length': '200'}),
            'opis_problemu': ('django.db.models.fields.TextField', [], {}),
            'organizacja': ('django.db.models.fields.CharField', [], {'default': "'Niewiadomo'", 'max_length': '200'}),
            'plec': ('django.db.models.fields.CharField', [], {'default': "'Niewiadomo'", 'max_length': '200'}),
            'propozycja_dotyczy': ('django.db.models.fields.CharField', [], {'default': "'Niewiadomo'", 'max_length': '200'}),
            'skad_jestes': ('django.db.models.fields.CharField', [], {'default': "'Niewiadomo'", 'max_length': '200'}),
            'stopien_instruktorski': ('django.db.models.fields.CharField', [], {'default': "'Niewiadomo'", 'max_length': '200'})
        },
        u'base.tradycja': {
            'Meta': {'object_name': 'Tradycja'},
            'dodana_przez': ('django.db.models.fields.CharField', [], {'default': "'System'", 'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nazwa': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'opis': ('django.db.models.fields.TextField', [], {})
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