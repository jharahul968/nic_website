# Generated by Django 4.1.5 on 2023-02-01 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nic_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrument',
            name='image',
            field=models.ImageField(default='images/default', upload_to='images/'),
        ),
    ]