# Generated by Django 2.2.6 on 2019-11-09 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memorygame', '0008_auto_20191109_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionlog',
            name='status',
            field=models.CharField(choices=[('ASSIGNED', 'ASSIGNED_TO_USER'), ('ANSWERING', 'ANSWERING'), ('ANSWERED', 'ANSWERED'), ('EXPIRED', 'EXPIRED')], max_length=200),
        ),
    ]
