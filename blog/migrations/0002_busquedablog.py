# Generated by Django 4.0.3 on 2022-03-19 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusquedaBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partial_blog', models.CharField(max_length=100)),
            ],
        ),
    ]