# Generated by Django 2.2.9 on 2020-01-06 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0003_voter_polls'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='slug',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]