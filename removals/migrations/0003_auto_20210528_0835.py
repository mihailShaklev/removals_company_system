# Generated by Django 3.1.5 on 2021-05-28 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('removals', '0002_auto_20210528_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='final_cost',
            field=models.IntegerField(),
        ),
    ]
