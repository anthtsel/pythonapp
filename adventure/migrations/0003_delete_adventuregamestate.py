# Generated by Django 5.0.1 on 2024-01-10 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0002_remove_adventuregamestate_game_result_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AdventureGameState',
        ),
    ]
