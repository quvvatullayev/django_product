# Generated by Django 4.1.1 on 2022-10-12 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_remove_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.TextField(default='exit'),
            preserve_default=False,
        ),
    ]