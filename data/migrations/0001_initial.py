# Generated by Django 3.2.4 on 2021-06-06 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=150)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
    ]