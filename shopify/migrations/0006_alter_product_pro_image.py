# Generated by Django 4.2.1 on 2023-06-27 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopify', '0005_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pro_image',
            field=models.ImageField(default='', upload_to='uploads/product/'),
            preserve_default=False,
        ),
    ]
