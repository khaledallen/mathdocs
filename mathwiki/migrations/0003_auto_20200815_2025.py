# Generated by Django 3.0 on 2020-08-15 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mathwiki', '0002_auto_20200815_2017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Axiom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('statement', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='definition',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='theorem',
            old_name='title',
            new_name='name',
        ),
    ]
