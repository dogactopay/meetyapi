# Generated by Django 4.0.5 on 2022-06-19 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('meetings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetings',
            name='tutor',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tutor_meetings', to='users.tutor'),
            preserve_default=False,
        ),
    ]
