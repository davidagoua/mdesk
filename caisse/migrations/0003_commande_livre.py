# Generated by Django 2.2.9 on 2020-06-03 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caisse', '0002_auto_20200603_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='livre',
            field=models.BooleanField(default=False),
        ),
    ]