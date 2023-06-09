# Generated by Django 4.1.3 on 2023-04-22 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=50)),
                ('contact_number', models.IntegerField()),
                ('email_address', models.EmailField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=150)),
            ],
        ),
    ]
