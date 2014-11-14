# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table(u'project_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('founder', self.gf('django.db.models.fields.related.ForeignKey')(related_name='projects_owned', to=orm['my_user.MyUser'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('display_image', self.gf('django.db.models.fields.files.ImageField')(default='img/default/project.jpg', max_length=100)),
            ('short_description', self.gf('django.db.models.fields.TextField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'project', ['Project'])

        # Adding M2M table for field participants on 'Project'
        m2m_table_name = db.shorten_name(u'project_project_participants')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'project.project'], null=False)),
            ('myuser', models.ForeignKey(orm[u'my_user.myuser'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'myuser_id'])

        # Adding model 'Vacancy'
        db.create_table(u'project_vacancy', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='vacancies', to=orm['project.Project'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('total', self.gf('django.db.models.fields.IntegerField')()),
            ('available', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'project', ['Vacancy'])

        # Adding model 'Application'
        db.create_table(u'project_application', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='applications', to=orm['my_user.MyUser'])),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='applications', to=orm['project.Project'])),
            ('pitch', self.gf('django.db.models.fields.TextField')()),
            ('result', self.gf('django.db.models.fields.CharField')(default='W', max_length=1)),
        ))
        db.send_create_signal(u'project', ['Application'])

        # Adding model 'Participation'
        db.create_table(u'project_participation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='positions', to=orm['my_user.MyUser'])),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(related_name='positions', to=orm['project.Project'])),
        ))
        db.send_create_signal(u'project', ['Participation'])

        # Adding model 'Title'
        db.create_table(u'project_title', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('participation', self.gf('django.db.models.fields.related.ForeignKey')(related_name='titles', to=orm['project.Participation'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'project', ['Title'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table(u'project_project')

        # Removing M2M table for field participants on 'Project'
        db.delete_table(db.shorten_name(u'project_project_participants'))

        # Deleting model 'Vacancy'
        db.delete_table(u'project_vacancy')

        # Deleting model 'Application'
        db.delete_table(u'project_application')

        # Deleting model 'Participation'
        db.delete_table(u'project_participation')

        # Deleting model 'Title'
        db.delete_table(u'project_title')


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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'my_user.myuser': {
            'Meta': {'object_name': 'MyUser'},
            'avatar': ('django.db.models.fields.files.ImageField', [], {'default': "'img/default/user.jpg'", 'max_length': '100'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {}),
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
        u'project.application': {
            'Meta': {'object_name': 'Application'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pitch': ('django.db.models.fields.TextField', [], {}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'applications'", 'to': u"orm['project.Project']"}),
            'result': ('django.db.models.fields.CharField', [], {'default': "'W'", 'max_length': '1'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'applications'", 'to': u"orm['my_user.MyUser']"})
        },
        u'project.participation': {
            'Meta': {'object_name': 'Participation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'positions'", 'to': u"orm['project.Project']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'positions'", 'to': u"orm['my_user.MyUser']"})
        },
        u'project.project': {
            'Meta': {'object_name': 'Project'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'display_image': ('django.db.models.fields.files.ImageField', [], {'default': "'img/default/project.jpg'", 'max_length': '100'}),
            'founder': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects_owned'", 'to': u"orm['my_user.MyUser']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participants': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'projects_participated'", 'blank': 'True', 'to': u"orm['my_user.MyUser']"}),
            'short_description': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'project.title': {
            'Meta': {'object_name': 'Title'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'titles'", 'to': u"orm['project.Participation']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'project.vacancy': {
            'Meta': {'object_name': 'Vacancy'},
            'available': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'vacancies'", 'to': u"orm['project.Project']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'total': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['project']