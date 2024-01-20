# Generated by Django 5.0.1 on 2024-01-20 04:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adventure', '0010_remove_scene_options_delete_option_delete_scene'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artifact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('riddle', models.TextField()),
                ('riddle_answer', models.CharField(max_length=255)),
                ('directions', models.JSONField(default=dict)),
                ('artifact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adventure.artifact')),
                ('connected_room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='adventure.room')),
            ],
        ),
    ]