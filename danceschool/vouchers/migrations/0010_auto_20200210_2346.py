# Generated by Django 2.2.6 on 2020-02-11 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vouchers', '0009_auto_20200113_2233'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='voucher',
            options={'permissions': (('generate_and_email_vouchers', 'Can generate and email vouchers using the quick voucher email view.'),), 'verbose_name': 'Voucher', 'verbose_name_plural': 'Vouchers'},
        ),
    ]
