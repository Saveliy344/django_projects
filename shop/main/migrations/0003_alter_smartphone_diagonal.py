# Generated by Django 4.0.1 on 2022-01-27 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_smartphone_alter_cartproduct_cost_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartphone',
            name='diagonal',
            field=models.DecimalField(decimal_places=2, max_digits=2, verbose_name='Диагональ, дюймы'),
        ),
    ]
