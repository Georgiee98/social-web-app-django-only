# Generated by Django 4.2.1 on 2023-05-12 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_comment_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='posted_by',
            field=models.CharField(default='georgi', max_length=255),
            preserve_default=False,
        ),
    ]
