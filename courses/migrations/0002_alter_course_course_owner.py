# Generated by Django 4.0.5 on 2022-06-19 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_owner',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='course_owner_name', to='users.tutor'),
        ),
    ]
