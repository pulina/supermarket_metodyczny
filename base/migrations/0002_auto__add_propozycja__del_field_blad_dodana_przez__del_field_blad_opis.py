# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Propozycja'
        db.create_table(u'base_propozycja', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nazwa', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('druzyna', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('dodana_przez', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('opis', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'base', ['Propozycja'])

        # Adding M2M table for field narzedzie on 'Propozycja'
        m2m_table_name = db.shorten_name(u'base_propozycja_narzedzie')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('propozycja', models.ForeignKey(orm[u'base.propozycja'], null=False)),
            ('narzedzia', models.ForeignKey(orm[u'base.narzedzia'], null=False))
        ))
        db.create_unique(m2m_table_name, ['propozycja_id', 'narzedzia_id'])

        # Deleting field 'Blad.dodana_przez'
        db.delete_column(u'base_blad', 'dodana_przez_id')

        # Deleting field 'Blad.opis'
        db.delete_column(u'base_blad', 'opis')

        # Deleting field 'Blad.nazwa'
        db.delete_column(u'base_blad', 'nazwa')

        # Deleting field 'Blad.id'
        db.delete_column(u'base_blad', u'id')

        # Adding field 'Blad.propozycja_ptr'
        db.add_column(u'base_blad', u'propozycja_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=2, to=orm['base.Propozycja'], unique=True, primary_key=True),
                      keep_default=False)

        # Removing M2M table for field narzedzie on 'Blad'
        db.delete_table(db.shorten_name(u'base_blad_narzedzie'))

        # Deleting field 'Pomysl.dodana_przez'
        db.delete_column(u'base_pomysl', 'dodana_przez_id')

        # Deleting field 'Pomysl.opis'
        db.delete_column(u'base_pomysl', 'opis')

        # Deleting field 'Pomysl.nazwa'
        db.delete_column(u'base_pomysl', 'nazwa')

        # Deleting field 'Pomysl.narzedzie'
        db.delete_column(u'base_pomysl', 'narzedzie_id')

        # Deleting field 'Pomysl.id'
        db.delete_column(u'base_pomysl', u'id')

        # Adding field 'Pomysl.propozycja_ptr'
        db.add_column(u'base_pomysl', u'propozycja_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=2, to=orm['base.Propozycja'], unique=True, primary_key=True),
                      keep_default=False)

        # Deleting field 'Tradycja.dodana_przez'
        db.delete_column(u'base_tradycja', 'dodana_przez_id')

        # Deleting field 'Tradycja.opis'
        db.delete_column(u'base_tradycja', 'opis')

        # Deleting field 'Tradycja.nazwa'
        db.delete_column(u'base_tradycja', 'nazwa')

        # Deleting field 'Tradycja.narzedzie'
        db.delete_column(u'base_tradycja', 'narzedzie_id')

        # Deleting field 'Tradycja.id'
        db.delete_column(u'base_tradycja', u'id')

        # Adding field 'Tradycja.propozycja_ptr'
        db.add_column(u'base_tradycja', u'propozycja_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=2, to=orm['base.Propozycja'], unique=True, primary_key=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Propozycja'
        db.delete_table(u'base_propozycja')

        # Removing M2M table for field narzedzie on 'Propozycja'
        db.delete_table(db.shorten_name(u'base_propozycja_narzedzie'))

        # Adding field 'Blad.dodana_przez'
        db.add_column(u'base_blad', 'dodana_przez',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'Blad.opis'
        db.add_column(u'base_blad', 'opis',
                      self.gf('django.db.models.fields.TextField')(default=2),
                      keep_default=False)

        # Adding field 'Blad.nazwa'
        db.add_column(u'base_blad', 'nazwa',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=200),
                      keep_default=False)

        # Adding field 'Blad.id'
        db.add_column(u'base_blad', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=2, primary_key=True),
                      keep_default=False)

        # Deleting field 'Blad.propozycja_ptr'
        db.delete_column(u'base_blad', u'propozycja_ptr_id')

        # Adding M2M table for field narzedzie on 'Blad'
        m2m_table_name = db.shorten_name(u'base_blad_narzedzie')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('blad', models.ForeignKey(orm[u'base.blad'], null=False)),
            ('narzedzia', models.ForeignKey(orm[u'base.narzedzia'], null=False))
        ))
        db.create_unique(m2m_table_name, ['blad_id', 'narzedzia_id'])

        # Adding field 'Pomysl.dodana_przez'
        db.add_column(u'base_pomysl', 'dodana_przez',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'Pomysl.opis'
        db.add_column(u'base_pomysl', 'opis',
                      self.gf('django.db.models.fields.TextField')(default=2),
                      keep_default=False)

        # Adding field 'Pomysl.nazwa'
        db.add_column(u'base_pomysl', 'nazwa',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=200),
                      keep_default=False)

        # Adding field 'Pomysl.narzedzie'
        db.add_column(u'base_pomysl', 'narzedzie',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['base.Narzedzia']),
                      keep_default=False)

        # Adding field 'Pomysl.id'
        db.add_column(u'base_pomysl', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=2, primary_key=True),
                      keep_default=False)

        # Deleting field 'Pomysl.propozycja_ptr'
        db.delete_column(u'base_pomysl', u'propozycja_ptr_id')

        # Adding field 'Tradycja.dodana_przez'
        db.add_column(u'base_tradycja', 'dodana_przez',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['auth.User']),
                      keep_default=False)

        # Adding field 'Tradycja.opis'
        db.add_column(u'base_tradycja', 'opis',
                      self.gf('django.db.models.fields.TextField')(default=2),
                      keep_default=False)

        # Adding field 'Tradycja.nazwa'
        db.add_column(u'base_tradycja', 'nazwa',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=200),
                      keep_default=False)

        # Adding field 'Tradycja.narzedzie'
        db.add_column(u'base_tradycja', 'narzedzie',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['base.Narzedzia']),
                      keep_default=False)

        # Adding field 'Tradycja.id'
        db.add_column(u'base_tradycja', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=2, primary_key=True),
                      keep_default=False)

        # Deleting field 'Tradycja.propozycja_ptr'
        db.delete_column(u'base_tradycja', u'propozycja_ptr_id')


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
            'Meta': {'object_name': 'Pomysl', '_ormbases': [u'base.Propozycja']},
            u'propozycja_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['base.Propozycja']", 'unique': 'True', 'primary_key': 'True'}),
            'zaakceptowany': ('django.db.models.fields.BooleanField', [], {})
        },
        u'base.propozycja': {
            'Meta': {'object_name': 'Propozycja'},
            'dodana_przez': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'druzyna': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'narzedzie': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['base.Narzedzia']", 'symmetrical': 'False'}),
            'nazwa': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'opis': ('django.db.models.fields.TextField', [], {})
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