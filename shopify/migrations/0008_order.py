# Generated by Django 4.2.1 on 2023-07-05 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopify', '0007_rename_category_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('mobile', models.BigIntegerField()),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopify.registrations')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopify.product')),
            ],
        ),
    ]
