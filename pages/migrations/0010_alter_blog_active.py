# Generated by Django 4.1.5 on 2023-02-10 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_alter_blog_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
