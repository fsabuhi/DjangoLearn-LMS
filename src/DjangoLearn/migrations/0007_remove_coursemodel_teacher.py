# Generated by Django 4.2.4 on 2023-09-28 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoLearn', '0006_coursemodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursemodel',
            name='teacher',
        ),
    ]
