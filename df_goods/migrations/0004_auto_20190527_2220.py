# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0003_auto_20190527_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='gpic',
            field=models.ImageField(upload_to='df_goods'),
        ),
    ]
