# Generated by Django 2.0 on 2021-10-25 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20211021_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='users_new',
            name='otp',
            field=models.CharField(max_length=6, null=True),
        ),
    ]
