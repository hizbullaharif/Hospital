# Generated by Django 3.1.5 on 2021-03-28 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sadmin', '0013_homerent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homerent',
            name='amount',
            field=models.IntegerField(verbose_name='Total Amount'),
        ),
        migrations.AlterField(
            model_name='homerent',
            name='is_paid',
            field=models.BooleanField(default=False, verbose_name='Paid or Not'),
        ),
        migrations.AlterField(
            model_name='homerent',
            name='month',
            field=models.DateField(verbose_name='Month`s Name'),
        ),
        migrations.AlterField(
            model_name='homerent',
            name='paid_by',
            field=models.CharField(max_length=200, null=True, verbose_name='Paid By'),
        ),
        migrations.AlterField(
            model_name='homerent',
            name='paid_to',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Paid To'),
        ),
    ]