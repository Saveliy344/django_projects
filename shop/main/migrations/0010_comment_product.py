# Generated by Django 4.0.1 on 2022-02-08 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.product', verbose_name='Продукт'),
            preserve_default=False,
        ),
    ]
