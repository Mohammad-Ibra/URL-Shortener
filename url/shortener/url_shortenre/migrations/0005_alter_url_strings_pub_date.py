# Generated by Django 3.2.5 on 2021-07-05 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortenre', '0004_url_strings_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url_strings',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]