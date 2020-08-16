# Generated by Django 3.0 on 2020-08-15 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mathwiki', '0004_auto_20200815_2126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='axiom',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='mathematicalobject',
            name='contains',
            field=models.ManyToManyField(related_name='_mathematicalobject_contains_+', to='mathwiki.MathematicalObject'),
        ),
        migrations.AddField(
            model_name='mathematicalobject',
            name='parent_objects',
            field=models.ManyToManyField(related_name='_mathematicalobject_parent_objects_+', to='mathwiki.MathematicalObject'),
        ),
        migrations.CreateModel(
            name='MathematicalProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('statement', models.TextField()),
                ('applies_to', models.ManyToManyField(to='mathwiki.MathematicalObject')),
            ],
        ),
        migrations.AddField(
            model_name='mathematicalobject',
            name='properties',
            field=models.ManyToManyField(to='mathwiki.MathematicalProperty'),
        ),
    ]