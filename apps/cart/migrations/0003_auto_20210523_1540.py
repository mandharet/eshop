# Generated by Django 3.0.5 on 2021-05-23 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_productimagesfiles_productimagesurl'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productimagesfiles',
            old_name='image_file1',
            new_name='image_file',
        ),
        migrations.RenameField(
            model_name='productimagesurl',
            old_name='image_url1',
            new_name='image_url',
        ),
        migrations.RemoveField(
            model_name='productimagesfiles',
            name='image_file2',
        ),
        migrations.RemoveField(
            model_name='productimagesfiles',
            name='image_file3',
        ),
        migrations.RemoveField(
            model_name='productimagesurl',
            name='image_url2',
        ),
        migrations.RemoveField(
            model_name='productimagesurl',
            name='image_url3',
        ),
    ]
