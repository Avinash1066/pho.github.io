# Generated by Django 4.0.5 on 2022-06-28 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itsp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cleaning',
            name='Contact_number',
            field=models.IntegerField(default=0),
        ),
    ]
