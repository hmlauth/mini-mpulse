# Generated by Django 3.1.5 on 2021-01-07 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hcore', '0003_auto_20210107_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='member',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
