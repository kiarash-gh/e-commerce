# Generated by Django 5.1.1 on 2024-09-18 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='subject',
            field=models.CharField(default='test', max_length=100),
            preserve_default=False,
        ),
    ]
