# Generated by Django 4.1.3 on 2022-12-27 06:17

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_cart_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttributeType',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AttributeValue',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('value', models.CharField(blank=True, max_length=50)),
                ('images', models.ImageField(upload_to='products')),
                ('atrib', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.attributetype')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
