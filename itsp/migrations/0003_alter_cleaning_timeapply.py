# Generated by Django 4.0.5 on 2022-06-28 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itsp', '0002_cleaning_contact_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cleaning',
            name='timeapply',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]