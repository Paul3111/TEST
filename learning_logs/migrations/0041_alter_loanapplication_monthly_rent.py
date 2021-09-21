# Generated by Django 3.2.7 on 2021-09-19 10:28

from decimal import Decimal
import django.core.validators
from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0040_auto_20210919_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanapplication',
            name='monthly_rent',
            field=djmoney.models.fields.MoneyField(decimal_places=0, default=Decimal('0'), default_currency='GBP', max_digits=11, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]