# Generated by Django 5.0.2 on 2024-04-10 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veg', '0002_alter_recipies_recipies_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipies',
            name='recipie_image',
            field=models.ImageField(upload_to='veg/static'),
        ),
    ]