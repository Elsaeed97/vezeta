# Generated by Django 3.0.4 on 2020-04-10 14:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200410_0016'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='joined_us',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='وقت الانضمام :'),
            preserve_default=False,
        ),
    ]