# Generated by Django 3.2.4 on 2021-07-05 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='description',
            field=models.CharField(choices=[('CH', 'Checking'), ('SA', 'Saving'), ('CC', 'Credit Card')], default='Checking', max_length=100),
        ),
    ]
