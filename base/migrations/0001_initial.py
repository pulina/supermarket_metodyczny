# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Blad'
        db.create_table(u'base_blad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nazwa', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('opis', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('szkodliwosc', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'base', ['Blad'])

        # Adding model 'Pomysl'
        db.create_table(u'base_pomysl', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nazwa', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('zgodnosc_z_metoda', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('skutecznosc_base', self.gf('django.db.models.fields.IntegerField')()),
            ('opis', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('wiek', self.gf('django.db.models.fields.IntegerField')()),
            ('zaakceptowany', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'base', ['Pomysl'])

        # Adding M2M table for field blady on 'Pomysl'
        m2m_table_name = db.shorten_name(u'base_pomysl_blady')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pomysl', models.ForeignKey(orm[u'base.pomysl'], null=False)),
            ('blad', models.ForeignKey(orm[u'base.blad'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pomysl_id', 'blad_id'])

        # Adding model 'Komentarz'
        db.create_table(u'base_komentarz', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('autor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('zawartosc', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('data_publikacji', self.gf('django.db.models.fields.DateTimeField')()),
            ('pomysl', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['base.Pomysl'])),
            ('ocena', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'base', ['Komentarz'])

        # Adding model 'Tradycja'
        db.create_table(u'base_tradycja', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('opis', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('nazwa', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'base', ['Tradycja'])

        # Adding M2M table for field pomysly on 'Tradycja'
        m2m_table_name = db.shorten_name(u'base_tradycja_pomysly')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tradycja', models.ForeignKey(orm[u'base.tradycja'], null=False)),
            ('pomysl', models.ForeignKey(orm[u'base.pomysl'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tradycja_id', 'pomysl_id'])

        # Adding model 'Forma'
        db.create_table(u'base_forma', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nazwa', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'base', ['Forma'])

        # Adding M2M table for field pomysly on 'Forma'
        m2m_table_name = db.shorten_name(u'base_forma_pomysly')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('forma', models.ForeignKey(orm[u'base.forma'], null=False)),
            ('pomysl', models.ForeignKey(orm[u'base.pomysl'], null=False))
        ))
        db.create_unique(m2m_table_name, ['forma_id', 'pomysl_id'])


    def backwards(self, orm):
        # Deleting model 'Blad'
        db.delete_table(u'base_blad')

        # Deleting model 'Pomysl'
        db.delete_table(u'base_pomysl')

        # Removing M2M table for field blady on 'Pomysl'
        db.delete_table(db.shorten_name(u'base_pomysl_blady'))

        # Deleting model 'Komentarz'
        db.delete_table(u'base_komentarz')

        # Deleting model 'Tradycja'
        db.delete_table(u'base_tradycja')

        # Removing M2M table for field pomysly on 'Tradycja'
        db.delete_table(db.shorten_name(u'base_tradycja_pomysly'))

        # Deleting model 'Forma'
        db.delete_table(u'base_forma')

        # Removing M2M table for field pomysly on 'Forma'
        db.delete_table(db.shorten_name(u'base_forma_pomysly'))


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
            'pomysly': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['base.Pomysl']", 'symmetrical': 'False'})
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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nazwa': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'opis': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'skutecznosc_base': ('django.db.models.fields.IntegerField', [], {}),
            'wiek': ('django.db.models.fields.IntegerField', [], {}),
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