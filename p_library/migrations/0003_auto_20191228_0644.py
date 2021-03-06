# Generated by Django 3.0.1 on 2019-12-28 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0002_auto_20191227_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='friend',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='p_library.Friend'),
        ),
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Фото'),
        ),
    ]
