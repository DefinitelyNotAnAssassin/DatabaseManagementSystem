# Generated by Django 3.2.6 on 2024-05-02 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdministrationDepartment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receivingform',
            name='full_name',
        ),
    ]