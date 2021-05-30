# Generated by Django 3.1.7 on 2021-05-29 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pools', '0009_auto_20210529_1835'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('house', models.CharField(max_length=100)),
                ('Member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pools.members')),
            ],
        ),
    ]