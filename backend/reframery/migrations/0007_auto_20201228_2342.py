# Generated by Django 3.1.4 on 2020-12-28 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reframery', '0006_auto_20201228_2340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='validate_code',
            field=models.CharField(default='kwlhcfct^f=_h#r1-zf+', max_length=255),
        ),
    ]
