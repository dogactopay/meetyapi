# Generated by Django 4.0.5 on 2022-06-19 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_course_course_owner'),
        ('meetings', '0003_alter_meetings_tutor'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetings',
            name='course',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_course_meetings', to='courses.course'),
        ),
    ]
