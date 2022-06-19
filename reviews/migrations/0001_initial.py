# Generated by Django 4.0.5 on 2022-06-19 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('review_text', models.TextField(default='', max_length=100)),
                ('review_score', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('user_reviews_from', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_reviews_from', to='users.users')),
                ('user_reviews_to', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_reviews_to', to='users.users')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
