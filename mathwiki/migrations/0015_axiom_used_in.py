# Generated by Django 3.1.6 on 2021-02-18 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mathwiki', '0014_mathematicalobject_used_in'),
    ]

    operations = [
        migrations.AddField(
            model_name='axiom',
            name='used_in',
            field=models.ManyToManyField(to='mathwiki.Theorem'),
        ),
    ]