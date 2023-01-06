# Generated by Django 4.1.3 on 2023-01-06 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ejemplo_dos', '0002_post_imagen_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('nombre', models.CharField(max_length=100)),
                ('texto', models.TextField(max_length=3000)),
                ('enviado_el', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
