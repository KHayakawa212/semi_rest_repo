# Generated by Django 2.2.4 on 2021-03-21 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semi_rest_tv_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='description',
            field=models.TextField(default='old show'),
            preserve_default=False,
        ),
    ]
