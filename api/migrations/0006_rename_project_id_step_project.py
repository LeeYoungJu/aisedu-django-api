# Generated by Django 4.0.2 on 2022-02-13 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_step_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='step',
            old_name='project_id',
            new_name='project',
        ),
    ]
