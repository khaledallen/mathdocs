# Generated by Django 3.1.6 on 2021-02-19 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mathwiki', '0015_axiom_used_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mathematicalobject',
            name='used_in',
            field=models.ManyToManyField(blank=True, to='mathwiki.Theorem'),
        ),
        migrations.AlterField(
            model_name='theorem',
            name='included_objects',
            field=models.ManyToManyField(blank=True, to='mathwiki.MathematicalObject'),
        ),
    ]