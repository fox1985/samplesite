# Generated by Django 3.2 on 2022-08-27 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0002_auto_20210418_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rubric',
            name='name',
            field=models.CharField(db_index=True, max_length=20, unique=True, verbose_name='Название'),
        ),
    ]