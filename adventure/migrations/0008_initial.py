# Generated by Django 5.0.1 on 2024-01-15 14:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adventure', '0007_delete_choice_delete_scene'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scene',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('option_1_text', models.CharField(max_length=255)),
                ('option_2_text', models.CharField(max_length=255)),
                ('option_1_destination', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='option_1', to='adventure.scene')),
                ('option_2_destination', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='option_2', to='adventure.scene')),
            ],
        ),
    ]