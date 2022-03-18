# Generated by Django 3.2.12 on 2022-03-06 08:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_kh', models.CharField(max_length=255)),
                ('name_en', models.CharField(max_length=255)),
                ('short_name', models.CharField(max_length=12)),
                ('contact_person', models.CharField(max_length=255)),
                ('contact_number', models.CharField(max_length=15)),
                ('contact_number_2', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=1000)),
                ('proile_picture', models.ImageField(blank=True, null=True, upload_to='media/branch/image', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png', 'ico', 'jpeg', 'giff'])])),
                ('website', models.CharField(max_length=60)),
                ('facebook', models.CharField(max_length=60)),
                ('telegram', models.CharField(max_length=15)),
                ('whatsapp', models.CharField(max_length=15)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
