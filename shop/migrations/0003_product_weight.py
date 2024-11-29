# Generated by Django 4.2.16 on 2024-11-29 11:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_translations'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.PositiveIntegerField(default=0, help_text='Weight in grams', validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
