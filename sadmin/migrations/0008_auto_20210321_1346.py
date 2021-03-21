# Generated by Django 3.1.5 on 2021-03-21 07:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sadmin', '0007_auto_20210321_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='month',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
    ]