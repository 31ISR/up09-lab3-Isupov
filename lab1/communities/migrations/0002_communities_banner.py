# Generated by Django 5.1.4 on 2024-12-12 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='communities',
            name='banner',
            field=models.ImageField(blank=True, default='ап.png', upload_to=''),
        ),
    ]