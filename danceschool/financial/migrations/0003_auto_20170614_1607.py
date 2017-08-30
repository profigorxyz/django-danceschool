# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-14 16:07
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20170614_1607'),
        ('financial', '0002_auto_20170425_0010'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='revenueitem',
            options={'ordering': ['-accrualDate'], 'permissions': (('export_financial_data', 'Export detailed financial transaction information to CSV'), ('view_finances_bymonth', 'View school finances month-by-month'), ('view_finances_byevent', 'View school finances by Event'), ('view_finances_detail', 'View school finances as detailed statement'))},
        ),
        migrations.RemoveField(
            model_name='revenueitem',
            name='eventregistration',
        ),
        migrations.RemoveField(
            model_name='revenueitem',
            name='purchasedVoucher',
        ),
        migrations.RemoveField(
            model_name='revenueitem',
            name='registration',
        ),
        migrations.AddField(
            model_name='revenueitem',
            name='invoiceItem',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.InvoiceItem'),
        ),
        migrations.AddField(
            model_name='revenueitem',
            name='taxes',
            field=models.FloatField(default=0, verbose_name='Taxes'),
        ),
        migrations.AlterField(
            model_name='expenseitem',
            name='payToName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='expenseitem',
            name='paymentMethod',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Payment method'),
        ),
        migrations.AlterField(
            model_name='revenueitem',
            name='adjustments',
            field=models.FloatField(default=0, help_text='Record any ex-post adjustments to the amount (e.g. refunds) in this field.  A positive amount increases the netRevenue, a negative amount reduces the netRevenue.', verbose_name='Adjustments'),
        ),
        migrations.AlterField(
            model_name='revenueitem',
            name='fees',
            field=models.FloatField(default=0, help_text='The sum of any transaction fees (e.g. Paypal fees) that were paid <strong>by us</strong>, and should therefore be subtracted from net revenue.', verbose_name='Fees'),
        ),
        migrations.AlterField(
            model_name='revenueitem',
            name='paymentMethod',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Payment method'),
        ),
        migrations.AlterField(
            model_name='revenueitem',
            name='total',
            field=models.FloatField(help_text='The total revenue received, net of any discounts or voucher uses.  This is what we actually receive.', validators=[django.core.validators.MinValueValidator(0)], verbose_name='Total'),
        ),
    ]