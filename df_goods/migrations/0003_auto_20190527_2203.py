# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0002_auto_20190527_1811'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GoodInfo',
            new_name='GoodsInfo',
        ),
    ]
