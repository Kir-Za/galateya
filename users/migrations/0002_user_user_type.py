# Generated by Django 2.1.5 on 2019-02-03 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('ur', 'Пользователь системы'), ('ac', 'Профиль анализатора')], default='ur', max_length=2, verbose_name='Тип пользователя'),
        ),
    ]