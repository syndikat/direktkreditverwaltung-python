# Generated by Django 3.0.8 on 2020-07-28 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dkapp', '0002_auto_20200726_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountingentry',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='accountingentry',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='accountingentry',
            name='updated_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='updated_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='contract',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='contract',
            name='updated_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='contractversion',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='contractversion',
            name='duration_months',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contractversion',
            name='duration_years',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contractversion',
            name='start',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='contractversion',
            name='updated_at',
            field=models.DateTimeField(),
        ),
    ]
