# Generated by Django 4.2.7 on 2023-11-09 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customuser_hours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='salary',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
