# Generated by Django 2.0.4 on 2018-09-26 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genome', '0003_auto_20180601_0901'),
    ]

    operations = [
        migrations.AddField(
            model_name='transcript',
            name='preferred_transcript',
            field=models.BooleanField(default=False),
        ),
    ]