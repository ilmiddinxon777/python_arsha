# Generated by Django 5.0.1 on 2024-01-24 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=85)),
                ('subject', models.CharField(max_length=75)),
                ('text', models.TextField(max_length=200)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='services',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
