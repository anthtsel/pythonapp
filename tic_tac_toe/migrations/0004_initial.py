# Generated by Django 5.0.1 on 2024-01-14 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tic_tac_toe', '0003_delete_tictactoegame'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicTacToeGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.CharField(default='---------', max_length=9)),
                ('player_turn', models.CharField(default='X', max_length=1)),
                ('winner', models.CharField(blank=True, max_length=1, null=True)),
                ('game_over', models.BooleanField(default=False)),
            ],
        ),
    ]
