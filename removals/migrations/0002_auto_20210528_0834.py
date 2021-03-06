# Generated by Django 3.1.5 on 2021-05-28 08:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('removals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default='user', max_length=64),
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='NAME', max_length=64)),
                ('phone', models.CharField(max_length=64)),
                ('email', models.CharField(max_length=64)),
                ('pickup', models.CharField(max_length=128)),
                ('delivery', models.CharField(max_length=128)),
                ('final_cost', models.IntegerField(max_length=64)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('pick_code', models.CharField(max_length=64)),
                ('deliv_code', models.CharField(max_length=64)),
                ('comment', models.TextField()),
                ('mover', models.CharField(max_length=64)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
