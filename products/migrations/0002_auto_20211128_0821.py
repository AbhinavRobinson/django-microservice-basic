# Generated by Django 3.2.9 on 2021-11-28 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='johndoe@nomail.com', max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='John Doe', max_length=200),
        ),
    ]
