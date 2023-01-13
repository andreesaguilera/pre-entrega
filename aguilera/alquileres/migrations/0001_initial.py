# Generated by Django 4.1.5 on 2023-01-12 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alquiler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('ambientes', models.IntegerField()),
                ('expensas', models.BooleanField()),
                ('imagen', models.CharField(max_length=100)),
            ],
        ),
    ]
