# Generated by Django 2.1.15 on 2020-01-02 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_ks', '0005_auto_20191231_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dinggou',
            name='chubanshe',
        ),
        migrations.AddField(
            model_name='dinggou',
            name='chubanshe',
            field=models.ManyToManyField(to='test_ks.Chubanshe'),
        ),
    ]
