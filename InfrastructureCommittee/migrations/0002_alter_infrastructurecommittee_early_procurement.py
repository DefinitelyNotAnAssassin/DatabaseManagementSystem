# Generated by Django 3.2.6 on 2024-06-19 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InfrastructureCommittee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infrastructurecommittee',
            name='early_procurement',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
