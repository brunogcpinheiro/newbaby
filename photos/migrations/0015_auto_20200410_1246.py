# Generated by Django 3.0.5 on 2020-04-10 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0014_remove_photo_responsaveis'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=64)),
                ('imagem', models.ImageField(upload_to='uploads/')),
            ],
        ),
        migrations.RenameModel(
            old_name='Category',
            new_name='Categoria',
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
        migrations.AddField(
            model_name='foto',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorias', to='photos.Categoria'),
        ),
    ]