# Generated by Django 4.1 on 2022-09-03 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0002_rename_news_news_1'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='news_1',
            new_name='news',
        ),
    ]
