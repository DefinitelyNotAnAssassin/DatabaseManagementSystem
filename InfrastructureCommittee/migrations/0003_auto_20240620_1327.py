# Generated by Django 3.2.6 on 2024-06-20 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InfrastructureCommittee', '0002_alter_infrastructurecommittee_early_procurement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infrastructurecommittee',
            name='bid_eval_date',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='infrastructurecommittee',
            name='bidding_date',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='infrastructurecommittee',
            name='contract_date',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='infrastructurecommittee',
            name='itb_date',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='infrastructurecommittee',
            name='noa_date',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='infrastructurecommittee',
            name='np_end',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='infrastructurecommittee',
            name='np_start',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='infrastructurecommittee',
            name='post_qua',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='infrastructurecommittee',
            name='pre_bid_date',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='infrastructurecommittee',
            name='pre_proc_date',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='infrastructurecommittee',
            name='reso_date',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
