# Generated by Django 3.0.6 on 2021-01-12 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='test',
        ),
    ]
