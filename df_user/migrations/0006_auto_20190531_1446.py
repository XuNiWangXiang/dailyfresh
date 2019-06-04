# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0005_goodsinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodsinfo',
            name='goods',
        ),
        migrations.DeleteModel(
            name='GoodsInfo',
        ),
    ]
