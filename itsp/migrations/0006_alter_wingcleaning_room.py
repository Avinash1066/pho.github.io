# Generated by Django 4.0.5 on 2022-07-02 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itsp', '0005_wingcleaning'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wingcleaning',
            name='Room',
            field=models.CharField(max_length=20, verbose_name='Any Room no. of the Wing'),
        ),
    ]