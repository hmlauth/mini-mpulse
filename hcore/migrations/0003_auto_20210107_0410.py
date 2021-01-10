# Generated by Django 3.1.5 on 2021-01-07 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hcore', '0002_auto_20210107_0352'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('account_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(blank=True, max_length=11)),
                ('client_member_id', models.CharField(max_length=30)),
                ('account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hcore.account')),
            ],
        ),
        migrations.DeleteModel(
            name='Members',
        ),
    ]
