# Generated by Django 2.2.5 on 2019-09-23 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiProje', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ozet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kelime', models.CharField(max_length=30)),
                ('frekans', models.FloatField()),
            ],
        ),
    ]
