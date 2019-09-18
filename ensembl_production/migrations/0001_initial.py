# Generated by Django 2.1.7 on 2019-09-18 15:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import ensembl_production.models

def initial_flask_app(apps, schema_editor):
    from django.core.management import call_command
    Group = apps.get_model('auth', 'Group')
    if Group.objects.count() == 0:
        call_command('loaddata', 'ensembl_production/fixtures/groups.json')
    call_command('loaddata', 'ensembl_production/fixtures/init.json')

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductionFlaskApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created on')),
                ('modified_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Last Update')),
                ('app_name', models.CharField(max_length=255, verbose_name='App display name')),
                ('app_url', models.URLField(max_length=255, verbose_name='App flask url')),
                ('app_theme', models.CharField(choices=[('336', 'Ensembl'), ('707080', 'Bacteria'), ('714486', 'Protists'), ('407253', 'Plants'), ('725A40', 'Fungi'), ('015365', 'Metazoa'), ('800066', 'Datachecks')], default='FFFFFF', max_length=6)),
                ('app_prod_url', models.CharField(max_length=200, unique=True, verbose_name='App Url')),
                ('app_groups', models.ManyToManyField(blank=True, to='auth.Group', db_constraint=False)),
                ('created_by', ensembl_production.models.SpanningForeignKey(blank=True, db_column='created_by', db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='productionflaskapp_created_by', related_query_name='productionflaskapp_creates', to=settings.AUTH_USER_MODEL)),
                ('modified_by', ensembl_production.models.SpanningForeignKey(blank=True, db_column='modified_by', db_constraint=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='productionflaskapp_modified_by', related_query_name='productionflaskapp_updates', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Flask App',
                'verbose_name_plural': 'Flask Apps',
                'db_table': 'flask_app',
            },
        ),
        migrations.RunPython(initial_flask_app, None),

    ]
