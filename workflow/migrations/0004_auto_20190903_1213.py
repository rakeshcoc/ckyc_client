# Generated by Django 2.2.4 on 2019-09-03 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0003_txn_flow_digitalid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='txn_flow',
            old_name='digitalID',
            new_name='digital_id',
        ),
    ]
