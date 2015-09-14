# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saumariapp', '0007_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clothing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clothing_type', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='image',
            name='img_description',
            field=models.CharField(default=b'none', max_length=1000),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='image',
            name='img_type',
            field=models.ForeignKey(default=1, to='saumariapp.Clothing'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='image',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
