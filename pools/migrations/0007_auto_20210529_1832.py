# Generated by Django 3.1.7 on 2021-05-29 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pools', '0006_auto_20210529_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='Member_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pools.members'),
        ),
    ]
