# Generated by Django 4.0.3 on 2022-04-06 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recognition', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='choice',
            field=models.CharField(choices=[('p', 'pdf'), ('t', 'txt')], default='p', max_length=1),
        ),
    ]
