# Generated by Django 3.2.11 on 2022-04-07 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='featured_image_url',
        ),
        migrations.AlterField(
            model_name='post',
            name='featured_image',
            field=models.URLField(blank=True, default='placeholder', max_length=1024, null=True, verbose_name='image'),
        ),
    ]
