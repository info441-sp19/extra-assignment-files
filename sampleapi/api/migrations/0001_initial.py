# Generated by Django 2.2 on 2019-04-24 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='name')),
                ('description', models.CharField(max_length=50, verbose_name='description')),
                ('breed', models.CharField(max_length=50, verbose_name='breed')),
            ],
        ),
    ]
