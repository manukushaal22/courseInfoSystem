# Generated by Django 2.2.4 on 2019-08-17 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseinformation', '0003_auto_20190817_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='username',
            field=models.CharField(default='', max_length=50),
        ),
    ]
