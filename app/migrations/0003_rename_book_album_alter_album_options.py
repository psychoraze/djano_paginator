# Generated by Django 5.0.4 on 2024-04-20 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_book_cover'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Book',
            new_name='Album',
        ),
        migrations.AlterModelOptions(
            name='album',
            options={'verbose_name': 'Album', 'verbose_name_plural': 'Albums'},
        ),
    ]