# Generated by Django 4.0.3 on 2022-04-18 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_useravatar_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useravatar',
            name='avatar',
            field=models.ImageField(blank=True, default='https://emser.es/wp-content/uploads/2016/08/usuario-sin-foto.png', null=True, upload_to='avatares'),
        ),
    ]
