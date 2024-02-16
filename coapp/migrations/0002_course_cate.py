# Generated by Django 5.0.1 on 2024-01-19 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='cate',
            field=models.IntegerField(choices=[(1, 'Beginner'), (2, 'Intermediate'), (3, 'Advanced')], default=0, verbose_name='Category'),
            preserve_default=False,
        ),
    ]