# Generated by Django 3.2.7 on 2021-09-12 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0020_alter_userinformation_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinformation',
            name='profile_picture',
            field=models.ImageField(upload_to='photos'),
        ),
    ]
