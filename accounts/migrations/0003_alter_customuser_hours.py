# Generated by Django 4.2.7 on 2023-11-09 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_hours_alter_customuser_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='hours',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
