# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Narzedzia'
        db.create_table(u'base_narzedzia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nazwa', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('opis', self.gf('django.db.models.fields.TextField')()),
            ('autor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'base', ['Narzedzia'])

        # Adding model 'Rok'
        db.create_table(u'base_rok', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(db_index=True, blank=True)),
            ('nazwa', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'base', ['Rok'])

        # Adding model 'Okres'
        db.create_table(u'base_okres', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sort_order', self.gf('django.db.models.fields.IntegerField')(db_index=True, blank=True)),
            ('nazwa', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('opis', self.gf('django.db.models.fields.TextField')()),
            ('rok', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.Rok'])),
        ))
        db.send_create_signal(u'base', ['Okres'])

        # Adding M2M table for field narzedzia on 'Okres'
        m2m_table_name = db.shorten_name(u'base_okres_narzedzia')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('okres', models.ForeignKey(orm[u'base.okres'], null=False)),
            ('narzedzia', models.ForeignKey(orm[u'base.narzedzia'], null=False))
        ))
        db.create_unique(m2m_table_name, ['okres_id', 'narzedzia_id'])

        # Adding model 'Blad'
        db.create_table(u'base_blad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nazwa', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('opis', self.gf('django.db.models.fields.TextField')()),
            ('dodana_przez', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'base', ['Blad'])

        # Adding M2M table for field narzedzie on 'Blad'
        m2m_table_name = db.shorten_name(u'base_blad_narzedzie')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('blad', models.ForeignKey(orm[u'base.blad'], null=False)),
            ('narzedzia', models.ForeignKey(orm[u'base.narzedzia'], null=False))
        ))
        db.create_unique(m2m_table_name, ['blad_id', 'narzedzia_id'])

        # Adding model 'Tradycja'
        db.create_table(u'base_tradycja', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nazwa', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('opis', self.gf('django.db.models.fields.TextField')()),
            ('dodana_przez', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('narzedzie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.Narzedzia'])),
        ))
        db.send_create_signal(u'base', ['Tradycja'])

        # Adding model 'Pomysl'
        db.create_table(u'base_pomysl', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nazwa', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('opis', self.gf('django.db.models.fields.TextField')()),
            ('zaakceptowany', self.gf('django.db.models.fields.BooleanField')()),
            ('dodana_przez', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('narzedzie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.Narzedzia'])),
        ))
        db.send_create_signal(u'base', ['Pomysl'])

        # Adding model 'Komentarz'
        db.create_table(u'base_komentarz', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('autor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('zawartosc', self.gf('django.db.models.fields.TextField')()),
            ('data_publikacji', self.gf('django.db.models.fields.DateTimeField')()),
            ('pomysl', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.Pomysl'])),
            ('ocena', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'base', ['Komentarz'])


    def backwards(self, orm):
        # Deleting model 'Narzedzia'
        db.delete_table(u'base_narzedzia')

        # Deleting model 'Rok'
        db.delete_table(u'base_rok')

        # Deleting model 'Okres'
        db.delete_table(u'base_okres')

        # Removing M2M table for field narzedzia on 'Okres'
        db.delete_table(db.shorten_name(u'base_okres_narzedzia'))

        # Deleting model 'Blad'
        db.delete_table(u'base_blad')

        # Removing M2M table for field narzedzie on 'Blad'
        db.delete_table(db.shorten_name(u'base_blad_narzedzie'))

        # Deleting model 'Tradycja'
        db.delete_table(u'base_tradycja')

        # Deleting model 'Pomysl'
        db.delete_table(u'base_pomysl')

        # Deleting model 'Komentarz'
        db.delete_table(u'base_komentarz')


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
            'dodana_przez': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'narzedzie': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['base.Narzedzia']", 'symmetrical': 'False'}),
            'nazwa': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'opis': ('django.db.models.fields.TextField', [], {})
        },
        u'base.komentarz': {
            'Meta': {'object_name': 'Komentarz'},
            'autor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'data_publikacji': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ocena': ('django.db.models.fields.IntegerField', [], {}),
            'pomysl': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.Pomysl']"}),
            'zawartosc': ('django.db.models.fields.TextField', [], {})
        },
        u'base.narzedzia': {
            'Meta': {'object_name': 'Narzedzia'},
            'autor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nazwa': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'opis': ('django.db.models.fields.TextField', [], {})
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
            'Meta': {'object_name': 'Pomysl'},
            'dodana_przez': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'narzedzie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.Narzedzia']"}),
            'nazwa': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'opis': ('django.db.models.fields.TextField', [], {}),
            'zaakceptowany': ('django.db.models.fields.BooleanField', [], {})
        },
        u'base.rok': {
            'Meta': {'ordering': "['sort_order']", 'object_name': 'Rok'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nazwa': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'})
        },
        u'base.tradycja': {
            'Meta': {'object_name': 'Tradycja'},
            'dodana_przez': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'narzedzie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['base.Narzedzia']"}),
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