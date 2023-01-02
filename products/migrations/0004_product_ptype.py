# Generated by Django 4.1.3 on 2022-12-06 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ptype',
            field=models.CharField(choices=[('Simple Product', 'simple'), ('With Variations', 'variations')], default=1, max_length=30),
            preserve_default=False,
        ),
    ]
