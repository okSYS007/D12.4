# Generated by Django 4.0.5 on 2022-06-25 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_rename_message_appointment_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='appointment_email',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
