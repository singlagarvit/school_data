# Generated by Django 3.2.4 on 2021-06-09 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20210609_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='sub1',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='sub2',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='sub3',
            field=models.IntegerField(),
        ),
    ]
