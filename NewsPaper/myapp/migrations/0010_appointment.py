# Generated by Django 4.0.5 on 2022-06-25 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_categorysubscribers_category_subscribers_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('client_name', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
    ]
