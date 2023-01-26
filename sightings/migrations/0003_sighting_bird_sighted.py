# Generated by Django 4.1.5 on 2023-01-19 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0001_initial'),
        ('sightings', '0002_alter_sighting_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='sighting',
            name='bird_sighted',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sightings', to='birds.bird'),
            preserve_default=False,
        ),
    ]
