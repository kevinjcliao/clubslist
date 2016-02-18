# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-18 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0002_auto_20160218_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='category',
            field=models.CharField(choices=[(b'AC', b'Academic'), (b'AF', b'Affinity Group'), (b'AW', b'Awareness and Activism'), (b'ME', b'Media and Publications'), (b'MU', b'Music'), (b'PR', b'Preprofessional Society'), (b'RE', b'Religious and Spiritugal Groups'), (b'SE', b'Service Groups'), (b'SP', b'Special Interests and Hobbies'), (b'OU', b'Sports and Outdoors Clubs'), (b'ST', b'Student Government Organization'), (b'AR', b'Visual and Performing Arts')], default=b'AC', max_length=2),
        ),
    ]