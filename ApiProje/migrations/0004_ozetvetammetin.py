# Generated by Django 2.2.5 on 2019-09-26 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiProje', '0003_auto_20190924_0855'),
    ]

    operations = [
        migrations.CreateModel(
            name='OzetveTamMetin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TamMetin', models.CharField(max_length=5000)),
                ('OzetMetin', models.CharField(max_length=1000)),
            ],
        ),
    ]