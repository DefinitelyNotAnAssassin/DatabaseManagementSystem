# Generated by Django 3.2.6 on 2024-06-20 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InfrastructureCommittee', '0004_auto_20240620_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='infrastructurecommittee',
            name='abc',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='infrastructurecommittee',
            name='bid_amount',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='infrastructurecommittee',
            name='calendar_days',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='infrastructurecommittee',
            name='duration',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
