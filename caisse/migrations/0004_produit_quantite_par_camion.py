# Generated by Django 2.2.9 on 2020-06-03 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caisse', '0003_commande_livre'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='quantite_par_camion',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
