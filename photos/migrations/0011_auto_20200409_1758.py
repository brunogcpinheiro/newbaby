# Generated by Django 3.0.5 on 2020-04-09 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0010_auto_20200408_2045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='palmas',
        ),
        migrations.AlterField(
            model_name='photo',
            name='imagem',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
