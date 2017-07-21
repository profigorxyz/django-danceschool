# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-20 19:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20170720_1945'),
        ('paypal', '0003_auto_20170717_1642'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaypalPaymentRecord',
            fields=[
                ('paymentrecord_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.PaymentRecord')),
                ('paymentId', models.CharField(max_length=50, unique=True, verbose_name='Paypal Payment ID')),
                ('payerId', models.CharField(blank=True, max_length=50, null=True, verbose_name='Paypal Payer ID')),
                ('status', models.CharField(blank=True, max_length=30, null=True, verbose_name='Current status')),
            ],
            options={
                'verbose_name': 'Paypal payment record',
                'verbose_name_plural': 'Payment records',
            },
            bases=('core.paymentrecord',),
        ),
        migrations.RemoveField(
            model_name='paymentrecord',
            name='invoice',
        ),
        migrations.DeleteModel(
            name='PaymentRecord',
        ),
    ]
