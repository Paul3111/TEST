# Generated by Django 3.2.6 on 2021-08-29 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0005_entry_topic_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='topic_name',
        ),
    ]
