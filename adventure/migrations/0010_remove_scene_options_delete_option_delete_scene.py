# Generated by Django 5.0.1 on 2024-01-15 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0009_rename_description_scene_text_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scene',
            name='options',
        ),
        migrations.DeleteModel(
            name='Option',
        ),
        migrations.DeleteModel(
            name='Scene',
        ),
    ]
