# Generated by Django 5.0.6 on 2024-08-12 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('Studentid', models.IntegerField(primary_key=True, serialize=False)),
                ('Studentname', models.CharField(max_length=100)),
                ('Studentage', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
