# Generated by Django 3.1 on 2020-08-14 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0008_auto_20200815_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writeblog',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]