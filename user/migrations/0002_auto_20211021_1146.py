# Generated by Django 2.0 on 2021-10-21 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='advertise',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ad_name', models.CharField(max_length=20)),
                ('ad_content', models.CharField(error_messages={'unique': 'This  content is already exists. Please  enter different content'}, max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='users_new',
            fields=[
                ('userId', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('mobilenumber', models.CharField(error_messages={'unique': 'This mobile number is already registered. Please login or enter different mobile number '}, max_length=10, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('emailid', models.EmailField(error_messages={'required': 'Please provide your email address.', 'unique': 'An account with this email exist.'}, max_length=50, unique=True)),
                ('friendslist', models.CharField(blank=True, max_length=20, null=True)),
                ('private', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]