# Generated by Django 4.1.3 on 2022-12-27 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_remove_attributevalue_atrib_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AttributeValue',
        ),
    ]
