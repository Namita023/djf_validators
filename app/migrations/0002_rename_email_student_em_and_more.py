# Generated by Django 5.0.6 on 2024-08-12 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='email',
            new_name='em',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Studentage',
            new_name='sage',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Studentid',
            new_name='sid',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Studentname',
            new_name='sname',
        ),
    ]
