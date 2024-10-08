# Generated by Django 5.0.7 on 2024-07-19 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0007_remove_shoe_photo_delete_photo_shoe_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoe',
            name='notexist',
            field=models.BooleanField(default=False, verbose_name='ناموجود'),
        ),
        migrations.AlterField(
            model_name='shoe',
            name='is_sale',
            field=models.BooleanField(default=False, verbose_name='تخفیف'),
        ),
        migrations.AlterField(
            model_name='shoe',
            name='sale_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='قیمت تخفیف'),
        ),
    ]
