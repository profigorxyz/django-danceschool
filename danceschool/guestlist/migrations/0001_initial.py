# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-02 19:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0024_staffmember_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuestList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Name')),
                ('sortOrder', models.CharField(choices=[('Last', 'Last name (default)'), ('First', 'First name'), ('Comp', 'Admission type (e.g. staff, registrant, other')], default='Last', max_length=5, verbose_name='Sort order')),
                ('includeStaff', models.BooleanField(default=True, verbose_name='Include all scheduled event staff')),
                ('includeRegistrants', models.BooleanField(default=True, verbose_name='Include event registrants')),
                ('eventCategories', models.ManyToManyField(blank=True, to='core.PublicEventCategory', verbose_name='Public event categories')),
                ('eventSessions', models.ManyToManyField(blank=True, to='core.EventSession', verbose_name='Event sessions')),
                ('individualEvents', models.ManyToManyField(blank=True, related_name='specifiedGuestLists', to='core.Event', verbose_name='Individual events')),
                ('seriesCategories', models.ManyToManyField(blank=True, to='core.SeriesCategory', verbose_name='Series categories')),
            ],
            options={
                'verbose_name': 'Guest list',
                'verbose_name_plural': 'Guest lists',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='GuestListComponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admissionRule', models.CharField(choices=[('Always', 'Always added to guest list'), ('EventOnly', 'Add if the person is a staff member for this event'), ('Day', 'Add if the person is a staff member on that day'), ('Week', 'Add if the person is a staff member in that week'), ('Month', 'Add if the person is a staff member in that month'), ('Year', 'Add if the person is a staff member in that year')], max_length=10, verbose_name='Event admission rule')),
                ('guestList', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guestlist.GuestList')),
                ('staffCategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.EventStaffCategory', verbose_name='Category of staff members')),
                ('staffMember', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.StaffMember', verbose_name='Individual staff member')),
            ],
            options={
                'verbose_name': 'Guest list component',
                'verbose_name_plural': 'Guest list components',
                'ordering': ('guestList', 'admissionRule'),
            },
        ),
        migrations.CreateModel(
            name='GuestListName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50, verbose_name='First name')),
                ('lastName', models.CharField(max_length=50, verbose_name='Last name')),
                ('guestList', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guestlist.GuestList')),
            ],
            options={
                'verbose_name': 'Manually-added guest',
                'verbose_name_plural': 'Manually added guests',
                'ordering': ('guestList', 'lastName', 'firstName'),
                'permissions': (('view_guestlist', 'Can view guest lists'),),
            },
        ),
        migrations.AlterUniqueTogether(
            name='guestlistcomponent',
            unique_together=set([('guestList', 'staffCategory', 'staffMember')]),
        ),
    ]