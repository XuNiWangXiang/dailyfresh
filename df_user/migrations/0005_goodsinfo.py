# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0005_remove_goodsinfo_gcontent'),
        ('df_user', '0004_auto_20190531_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('goods', models.ForeignKey(to='df_goods.GoodsInfo')),
            ],
        ),
    ]
