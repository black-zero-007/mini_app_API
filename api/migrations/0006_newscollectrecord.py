# Generated by Django 3.1.4 on 2021-03-03 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_topicviewerrecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsCollectRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.news', verbose_name='文章')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.userinfo', verbose_name='用户')),
            ],
        ),
    ]
