# Generated by Django 5.0.1 on 2024-01-20 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0011_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DungeonRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('directions', models.JSONField()),
            ],
        ),
        migrations.RemoveField(
            model_name='room',
            name='artifact',
        ),
        migrations.RemoveField(
            model_name='room',
            name='connected_room',
        ),
        migrations.DeleteModel(
            name='Artifact',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]