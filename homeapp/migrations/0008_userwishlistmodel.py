# Generated by Django 4.1.6 on 2023-02-09 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0007_userapplymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='userwishlistmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('service', models.CharField(max_length=20)),
                ('phone', models.IntegerField()),
                ('location', models.CharField(max_length=50)),
            ],
        ),
    ]
