# Generated by Django 2.2.9 on 2020-01-07 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0007_remove_voter_polls'),
        ('access', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultmodel',
            name='token',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='consultmodel',
            unique_together={('voter', 'poll')},
        ),
    ]