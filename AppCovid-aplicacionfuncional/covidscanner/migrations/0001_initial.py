# Generated by Django 4.0.1 on 2022-01-28 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=250, verbose_name='Email')),
                ('passports', models.FileField(upload_to='media/passports')),
            ],
        ),
    ]
