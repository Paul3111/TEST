# Generated by Django 3.2.7 on 2021-09-18 21:41

from decimal import Decimal
from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0029_auto_20210918_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanapplication',
            name='loan_amount',
            field=djmoney.models.fields.MoneyField(decimal_places=4, default=Decimal('0'), default_currency='GBP', max_digits=11),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='monthly_expenses',
            field=djmoney.models.fields.MoneyField(decimal_places=4, default=Decimal('0'), default_currency='GBP', max_digits=10),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='monthly_rent',
            field=djmoney.models.fields.MoneyField(decimal_places=4, default=Decimal('0'), default_currency='GBP', max_digits=10),
        ),
        migrations.AlterField(
            model_name='loanapplication',
            name='monthly_salary',
            field=djmoney.models.fields.MoneyField(decimal_places=4, default=Decimal('0'), default_currency='GBP', max_digits=10),
        ),
    ]
