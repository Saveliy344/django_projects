# Generated by Django 4.0.1 on 2022-01-27 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmartPhone',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main.product')),
                ('diagonal', models.PositiveIntegerField(verbose_name='Диагональ, дюймы')),
                ('colour', models.CharField(max_length=255, verbose_name='Цвет')),
                ('capacity', models.PositiveIntegerField(verbose_name='Ёмкость, мАч')),
                ('camera', models.PositiveIntegerField(verbose_name='Камера, Мпикс')),
                ('processor', models.CharField(max_length=255, verbose_name='Процессор')),
                ('ram', models.PositiveIntegerField(verbose_name='ОЗУ, Гб')),
                ('cores', models.PositiveIntegerField(verbose_name='Число ядер процессора')),
                ('memory', models.PositiveIntegerField(verbose_name='Встроенная память, Гб')),
                ('resolution', models.CharField(max_length=255, verbose_name='Разрешение экрана')),
            ],
            bases=('main.product',),
        ),
        migrations.AlterField(
            model_name='cartproduct',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=2, verbose_name='Стоимость, руб'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=2, verbose_name='Цена, руб'),
        ),
    ]
