# Generated by Django 4.1.5 on 2023-02-13 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_remove_categories_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ManyToManyField(to='pages.categories'),
        ),
    ]
