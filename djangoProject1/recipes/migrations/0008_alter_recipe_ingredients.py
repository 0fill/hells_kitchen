# Generated by Django 5.1.1 on 2024-10-31 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_rename_author_id_recipe_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.CharField(help_text='separated by comma', max_length=1024),
        ),
    ]
