# Generated by Django 5.0.1 on 2024-01-14 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tic_tac_toe', '0004_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TicTacToeGame',
        ),
    ]