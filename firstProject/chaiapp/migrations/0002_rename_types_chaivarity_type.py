# Generated by Django 5.2 on 2025-04-08 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chaiapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chaivarity',
            old_name='types',
            new_name='type',
        ),
    ]
