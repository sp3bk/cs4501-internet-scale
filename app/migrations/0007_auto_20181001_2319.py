# Generated by Django 2.1 on 2018-10-01 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20181001_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='borrower_rating_total',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='lender_rating_total',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
