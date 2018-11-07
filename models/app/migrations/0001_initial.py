# Generated by Django 2.1 on 2018-11-06 17:33

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authenticator',
            fields=[
                ('authenticator', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('date_created', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_date', models.DateTimeField(verbose_name='date borrowed')),
                ('borrow_days', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('condition', models.CharField(choices=[('E', 'E'), ('G', 'G'), ('O', 'O'), ('B', 'B')], default='G', max_length=1)),
                ('description', models.TextField()),
                ('price_per_day', models.DecimalField(decimal_places=2, max_digits=10)),
                ('max_borrow_days', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('currently_borrowed', models.BooleanField(blank=True, default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('score', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('overview', models.TextField()),
                ('zip_code', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{5}(?:[-\\s]\\d{4})?$')])),
                ('lender_rating_total', models.IntegerField(blank=True, default=0)),
                ('lender_rating_count', models.IntegerField(blank=True, default=0)),
                ('borrower_rating_total', models.IntegerField(blank=True, default=0)),
                ('borrower_rating_count', models.IntegerField(blank=True, default=0)),
                ('password', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='reviewee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_reviews', to='app.User'),
        ),
        migrations.AddField(
            model_name='review',
            name='reviewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='written_reviews', to='app.User'),
        ),
        migrations.AddField(
            model_name='item',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
        migrations.AddField(
            model_name='borrow',
            name='borrower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrowed_items', to='app.User'),
        ),
        migrations.AddField(
            model_name='borrow',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Item'),
        ),
        migrations.AddField(
            model_name='borrow',
            name='lender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lent_items', to='app.User'),
        ),
        migrations.AddField(
            model_name='authenticator',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User'),
        ),
    ]
