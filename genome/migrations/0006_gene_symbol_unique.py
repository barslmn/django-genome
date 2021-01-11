# Generated by Django 2.2.6 on 2019-10-31 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genome', '0005_add_important_gene_dates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gene',
            name='symbol',
            field=models.CharField(db_index=True, max_length=255, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='gene',
            unique_together=set(),
        ),
    ]