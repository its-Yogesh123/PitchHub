# Generated by Django 5.1.5 on 2025-03-10 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investor', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investorprofile',
            name='available_funds',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='investorprofile',
            name='investment_focus',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
