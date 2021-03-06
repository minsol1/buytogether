# Generated by Django 4.0.4 on 2022-06-09 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_user_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='userID',
            field=models.EmailField(max_length=200, primary_key=True, serialize=False),
        ),
    ]
