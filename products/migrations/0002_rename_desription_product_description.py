# Generated by Django 5.0.6 on 2024-05-15 00:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='desription',
            new_name='description',
        ),
    ]