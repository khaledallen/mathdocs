# Generated by Django 3.0 on 2020-09-02 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mathwiki', '0012_auto_20200828_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='theorem',
            name='references',
            field=models.ManyToManyField(blank=True, to='mathwiki.Theorem'),
        ),
    ]
