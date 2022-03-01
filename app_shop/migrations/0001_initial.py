# Generated by Django 4.0.2 on 2022-02-28 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('image', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=800)),
            ],
        ),
    ]
