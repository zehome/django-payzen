# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_payzen', '0004_auto_20141221_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentrequest',
            name='vads_currency',
            field=models.CharField(default=978, max_length=3, choices=[(b'036', b'Australian dollar'), (b'124', b'Canadian dollar'), (b'156', b'Chinese Yuan'), (b'208', b'Danish Krone'), (b'392', b'Japanese Yen'), (b'578', b'Norwegian Krone'), (b'752', b'Swedish Krona'), (b'756', b'Swiss franc'), (b'826', b'Pound sterling'), (b'840', b'American dollar'), (b'953', b'Franc Pacifique (CFP)'), (b'978', b'Euro')]),
        ),
        migrations.AlterField(
            model_name='paymentrequest',
            name='vads_cust_email',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='paymentrequest',
            name='vads_site_id',
            field=models.PositiveIntegerField(default=59095860),
        ),
        migrations.AlterField(
            model_name='paymentresponse',
            name='vads_cust_email',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
    ]
