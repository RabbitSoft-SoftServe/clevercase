# Generated by Django 4.2.6 on 2023-11-05 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0002_alter_category_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='color_save',
            field=models.CharField(blank=True, default='#0c854b66', max_length=100, null=True),
        ),
    ]