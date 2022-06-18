# Generated by Django 4.0.5 on 2022-06-18 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('denemeapp', '0001_initial'),
        ('tangible', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('balance_id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='denemeapp.users')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
