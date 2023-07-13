# Generated by Django 4.2.1 on 2023-06-25 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopify', '0002_registion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registrations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=50, null=True)),
                ('last_name', models.CharField(default='', max_length=50, null=True)),
                ('email', models.CharField(default='', max_length=50, null=True)),
                ('password', models.CharField(default='', max_length=50, null=True)),
                ('mobile', models.BigIntegerField()),
                ('gender', models.CharField(default='', max_length=50, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Registion',
        ),
    ]