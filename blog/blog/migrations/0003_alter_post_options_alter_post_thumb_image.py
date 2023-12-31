# Generated by Django 4.2.6 on 2023-11-07 14:07

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_file_upload'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='post',
            name='thumb_image',
            field=models.ImageField(blank=True, upload_to=blog.models.custom_image_path),
        ),
    ]
