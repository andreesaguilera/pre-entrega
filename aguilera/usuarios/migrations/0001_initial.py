# Generated by Django 4.1.5 on 2023-01-12 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
                ('password', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=100)),
            ],
        ),
    ]
