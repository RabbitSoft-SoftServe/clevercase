# Generated by Django 4.2.5 on 2023-11-21 20:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wallet', '0004_alter_category_currently_spent_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyDebts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debt_amount', models.IntegerField(default=0)),
                ('currency', models.CharField(choices=[('₴', '₴'), ('€', '€'), ('$', '$')], default='₴', max_length=2)),
                ('date_of_borrowing', models.DateTimeField(blank=True, default=datetime.datetime(2023, 11, 21, 22, 47, 11, 366136))),
                ('debt_repayment_date', models.DateTimeField(blank=True, null=True)),
                ('creditor_name', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OthersDebts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debt_amount', models.IntegerField(default=0)),
                ('currency', models.CharField(choices=[('₴', '₴'), ('€', '€'), ('$', '$')], default='₴', max_length=2)),
                ('date_of_borrowing', models.DateTimeField(blank=True, default=datetime.datetime(2023, 11, 21, 22, 47, 11, 366136))),
                ('debt_repayment_date', models.DateTimeField(blank=True, null=True)),
                ('debtor_name', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Currency',
        ),
        migrations.AlterField(
            model_name='category',
            name='color_save',
            field=models.CharField(default='#0c854b66', max_length=100),
        ),
        migrations.AlterField(
            model_name='category',
            name='currency',
            field=models.CharField(choices=[('₴', '₴'), ('€', '€'), ('$', '$')], default='₴', max_length=2),
        ),
        migrations.AlterField(
            model_name='category',
            name='currently_spent',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='category',
            name='date_of_rent',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date of rent'),
        ),
        migrations.AlterField(
            model_name='category',
            name='due_date',
            field=models.DateField(verbose_name='Due date'),
        ),
        migrations.AlterField(
            model_name='category',
            name='the_limit',
            field=models.IntegerField(default=0),
        ),
    ]
