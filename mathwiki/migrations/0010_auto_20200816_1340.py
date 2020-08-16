# Generated by Django 3.0 on 2020-08-16 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mathwiki', '0009_auto_20200816_0446'),
    ]

    operations = [
        migrations.AddField(
            model_name='axiom',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='mathematicalobject',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='mathematicalproperty',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='theorem',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]
