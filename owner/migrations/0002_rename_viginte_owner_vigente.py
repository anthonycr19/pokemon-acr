# Generated by Django 4.2.7 on 2023-11-12 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='owner',
            old_name='viginte',
            new_name='vigente',
        ),
    ]
