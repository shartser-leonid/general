# Generated by Django 2.2.6 on 2019-11-09 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memorygame', '0005_usermemoryquestionhistory_time_stamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermemoryquestionhistory',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
