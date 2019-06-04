# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('df_goods', '0005_remove_goodsinfo_gcontent'),
        ('df_cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartinfo',
            name='goods',
            field=models.ForeignKey(default=1, to='df_goods.GoodsInfo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cartinfo',
            name='user',
            field=models.ForeignKey(to='df_user.UserInfo'),
        ),
    ]
