# Generated by Django 4.1.5 on 2023-01-21 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_alter_blog_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='cover',
            field=models.ImageField(upload_to='blog_cover/'),
        ),
    ]
