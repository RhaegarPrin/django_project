# Generated by Django 3.1.7 on 2021-06-13 03:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pools', '0014_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='item_fk',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='pools.items'),
        ),
    ]
