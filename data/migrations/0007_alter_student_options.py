# Generated by Django 3.2.4 on 2021-06-10 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_schoolprofile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'permissions': [('can_update', 'Can update the data of students')]},
        ),
    ]
