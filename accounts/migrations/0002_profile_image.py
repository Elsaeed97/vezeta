# Generated by Django 3.0.4 on 2020-04-08 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default=1, upload_to='profile', verbose_name='الصورة الشخصية :'),
            preserve_default=False,
        ),
    ]
