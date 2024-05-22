# Generated by Django 5.0.6 on 2024-05-22 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='status',
            field=models.CharField(choices=[('in_stock', 'In Stock'), ('in_use', 'In Use')], default='in_stock', max_length=10),
        ),
    ]