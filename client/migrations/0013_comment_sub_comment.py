# Generated by Django 2.2.2 on 2019-07-02 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0012_auto_20190702_0915'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='sub_comment',
            field=models.IntegerField(default=0),
        ),
    ]
