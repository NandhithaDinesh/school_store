# Generated by Django 4.2.7 on 2023-11-08 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0003_alter_formentry_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formentry',
            name='dob',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='formentry',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]