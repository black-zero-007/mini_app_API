# Generated by Django 3.1.4 on 2021-03-04 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_newscollectrecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='collect_count',
            field=models.PositiveIntegerField(default=0, verbose_name='收藏数'),
        ),
    ]
