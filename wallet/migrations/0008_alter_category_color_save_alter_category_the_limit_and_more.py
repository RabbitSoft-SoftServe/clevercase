# Generated by Django 4.2.6 on 2023-12-02 11:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wallet', '0007_merge_20231126_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='color_save',
            field=models.CharField(default='rgba(176,151,218,255)', max_length=100),
        ),
        migrations.AlterField(
            model_name='category',
            name='the_limit',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='mydebts',
            name='date_of_borrowing',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 2, 13, 28, 21, 650275)),
        ),
        migrations.AlterField(
            model_name='othersdebts',
            name='date_of_borrowing',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 2, 13, 28, 21, 651276)),
        ),
        migrations.CreateModel(
            name='Spendings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='DD.MM.YYYY')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
