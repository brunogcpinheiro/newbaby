# Generated by Django 3.0.5 on 2020-04-08 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_auto_20200408_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='photos.Category'),
        ),
    ]
