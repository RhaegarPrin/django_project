# Generated by Django 3.1.7 on 2021-06-14 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pools', '0016_auto_20210613_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='item_note',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
