# Generated by Django 3.2.7 on 2021-09-20 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0049_loanapplication_interest_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanapplication',
            name='monthly_payment',
            field=models.FloatField(default=0.0, null=True),
        ),
    ]
