# Generated by Django 4.2 on 2023-10-28 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_remove_product_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='color',
            old_name='color_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='color',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='gallery'),
        ),
    ]
