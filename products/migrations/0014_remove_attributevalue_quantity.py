# Generated by Django 4.1.3 on 2022-12-27 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_attributevalue'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attributevalue',
            name='quantity',
        ),
    ]
