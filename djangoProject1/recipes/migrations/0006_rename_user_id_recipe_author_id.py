# Generated by Django 5.1.1 on 2024-10-24 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_recipe_user_id_alter_recipe_ingredients'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='user_id',
            new_name='author_id',
        ),
    ]
