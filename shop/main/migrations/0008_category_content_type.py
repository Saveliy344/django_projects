# Generated by Django 4.0.1 on 2022-02-04 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('main', '0007_product_time_create_product_time_update_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='content_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
            preserve_default=False,
        ),
    ]
