# Generated by Django 5.1.1 on 2024-10-16 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_alter_recipe_difficulty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.CharField(max_length=1024),
        ),
    ]