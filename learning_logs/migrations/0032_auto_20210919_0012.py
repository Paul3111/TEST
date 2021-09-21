# Generated by Django 3.2.7 on 2021-09-18 23:12

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0031_auto_20210918_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanapplication',
            name='loan_amount',
            field=djmoney.models.fields.MoneyField(decimal_places=0, default_currency='GBP', max_digits=11, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='loan_term',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=100),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='monthly_expenses',
            field=djmoney.models.fields.MoneyField(decimal_places=4, default=Decimal('0'), default_currency='GBP', max_digits=10, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='monthly_rent',
            field=djmoney.models.fields.MoneyField(decimal_places=4, default=Decimal('0'), default_currency='GBP', max_digits=10, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='monthly_salary',
            field=djmoney.models.fields.MoneyField(decimal_places=4, default=Decimal('0'), default_currency='GBP', max_digits=10, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]