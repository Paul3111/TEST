# Generated by Django 3.2.6 on 2021-09-07 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0011_auto_20210906_2319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinformation',
            name='customer_id',
        ),
        migrations.AddField(
            model_name='userinformation',
            name='profile_picture',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]