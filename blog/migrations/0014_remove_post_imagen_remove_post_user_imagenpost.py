# Generated by Django 4.0.3 on 2022-04-12 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0013_post_imagen_delete_imagenpost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='imagen',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.CreateModel(
            name='ImagenPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='blog/images')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
