# Generated by Django 4.0 on 2021-12-24 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Image',
            new_name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.PositiveIntegerField(blank=True, db_index=True, default=0, verbose_name='like'),
        ),
    ]
