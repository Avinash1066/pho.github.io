# Generated by Django 4.0.5 on 2022-06-28 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itsp', '0003_alter_cleaning_timeapply'),
    ]

    operations = [
        migrations.AddField(
            model_name='cleaning',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='cleaning',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]