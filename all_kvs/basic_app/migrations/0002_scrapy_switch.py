# Generated by Django 3.1.5 on 2021-02-07 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scrapy_Switch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('switch', models.BooleanField()),
                ('last_on', models.DateTimeField(auto_now=True, verbose_name='date_published')),
            ],
        ),
    ]
