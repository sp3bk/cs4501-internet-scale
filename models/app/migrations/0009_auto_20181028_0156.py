# Generated by Django 2.1 on 2018-10-28 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20181028_0156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='authenticator',
            name='id',
        ),
        migrations.AlterField(
            model_name='authenticator',
            name='authenticator',
            field=models.CharField(max_length=64, primary_key=True, serialize=False),
        ),
    ]