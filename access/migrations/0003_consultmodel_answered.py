# Generated by Django 2.2.9 on 2020-01-08 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0002_auto_20200106_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultmodel',
            name='answered',
            field=models.BooleanField(default=False),
        ),
    ]
