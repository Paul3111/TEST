# Generated by Django 3.2.7 on 2021-09-13 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0025_customermessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customermessage',
            name='customer_message',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='customermessage',
            name='customer_message_subject',
            field=models.TextField(max_length=200),
        ),
    ]
