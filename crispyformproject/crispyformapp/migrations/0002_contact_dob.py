# Generated by Django 4.1.3 on 2023-08-07 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crispyformapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='DOB',
            field=models.DateField(null=True, verbose_name='Date Of Birth'),
        ),
    ]
