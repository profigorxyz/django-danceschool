# Generated by Django 2.2.6 on 2020-01-05 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prerequisites', '0005_merge_20191028_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requirementitem',
            name='requirement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='prerequisites.Requirement', verbose_name='Requirement'),
        ),
    ]