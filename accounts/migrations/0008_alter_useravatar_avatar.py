# Generated by Django 4.0.3 on 2022-04-18 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_useravatar_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useravatar',
            name='avatar',
            field=models.ImageField(blank=True, default='Messi.jpg', null=True, upload_to='avatares'),
        ),
    ]
