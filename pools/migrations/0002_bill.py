# Generated by Django 3.1.7 on 2021-04-09 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pools', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Member_id', models.IntegerField()),
                ('total', models.FloatField()),
                ('order_date', models.DateField()),
            ],
        ),
    ]