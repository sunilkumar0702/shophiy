# Generated by Django 4.2.1 on 2023-07-01 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopify', '0006_alter_product_pro_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Category',
            new_name='category',
        ),
    ]
