# Generated by Django 4.2.6 on 2023-12-02 11:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0008_alter_category_color_save_alter_category_the_limit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='spendings',
            name='categoryId',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mydebts',
            name='date_of_borrowing',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 2, 13, 49, 36, 689446)),
        ),
        migrations.AlterField(
            model_name='othersdebts',
            name='date_of_borrowing',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 12, 2, 13, 49, 36, 690448)),
        ),
    ]