# Generated by Django 4.2.7 on 2023-11-22 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=30)),
                ('docente', models.BooleanField(default=False)),
            ],
        ),
    ]
