# Generated by Django 4.0.5 on 2022-06-18 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tangible', '0006_alter_balance_balance_alter_transaction_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='balance',
            old_name='user',
            new_name='user_balance',
        ),
    ]