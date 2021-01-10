# Generated by Django 3.1.5 on 2021-01-07 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hcore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(blank=True, max_length=11)),
                ('client_member_id', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]
