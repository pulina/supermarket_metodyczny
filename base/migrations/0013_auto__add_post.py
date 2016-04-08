# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Post'
        db.create_table(u'base_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Autor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('Tytul', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('Tekst', self.gf('django.db.models.fields.TextField')()),
            ('data_stworzenia', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('data_publikacji', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'base', ['Post'])


    def backwards(self, orm):
        # Deleting model 'Post'
        db.delete_table(u'base_post')


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
            'Meta': {'object_name': 'Blad', '_ormbases': [u'base.Propozycja']},
            u'propozycja_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['base.Propozycja']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'base.komentarz': {
            'Meta': {'object_name': 'Komentarz'},
            'autor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'data_publikacji': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ocena': ('django.db.models.fields.IntegerField', [], {}),
            'propozycja': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.Propozycja']"}),
            'zawartosc': ('django.db.models.fields.TextField', [], {})
        },
        u'base.narzedzia': {
            'Meta': {'object_name': 'Narzedzia'},
            '_autor': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'dodana_przez': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nazwa': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'opis': ('django.db.models.fields.TextField', [], {}),
            'zaakceptowany': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'base.okres': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'Okres'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'narzedzia': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['base.Narzedzia']", 'null': 'True', 'blank': 'True'}),
            'nazwa': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'opis': ('django.db.models.fields.TextField', [], {}),
            'rok': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.Rok']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'})
        },
        u'base.pomysl': {
            'Meta': {'object_name': 'Pomysl', '_ormbases': [u'base.Propozycja']},
            u'propozycja_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['base.Propozycja']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'base.post': {
            'Autor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'Meta': {'object_name': 'Post'},
            'Tekst': ('django.db.models.fields.TextField', [], {}),
            'Tytul': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'data_publikacji': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'data_stworzenia': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'base.propozycja': {
            'Meta': {'object_name': 'Propozycja'},
            '_autor': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'dodana_przez': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'druzyna': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'moment_wystapienia': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'narzedzie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.Narzedzia']"}),
            'nazwa': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'opis': ('django.db.models.fields.TextField', [], {}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'polymorphic_base.propozycja_set+'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'zaakceptowany': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'base.rok': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'Rok'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nazwa': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'})
        },
        u'base.tradycja': {
            'Meta': {'object_name': 'Tradycja', '_ormbases': [u'base.Propozycja']},
            u'propozycja_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['base.Propozycja']", 'unique': 'True', 'primary_key': 'True'})
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