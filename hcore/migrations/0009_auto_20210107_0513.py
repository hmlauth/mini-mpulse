# Generated by Django 3.1.5 on 2021-01-07 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hcore', '0008_auto_20210107_0509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='phone_number',
            field=models.CharField(max_length=11),
        ),
    ]
