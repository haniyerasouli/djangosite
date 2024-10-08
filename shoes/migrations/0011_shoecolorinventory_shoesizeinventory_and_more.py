# Generated by Django 5.0.7 on 2024-07-22 22:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0010_shoecolorsizeinventory_delete_shoecolorinventory'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoeColorInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoes.color')),
                ('shoe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoes.shoe')),
            ],
        ),
        migrations.CreateModel(
            name='ShoeSizeInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('shoe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoes.shoe')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shoes.color')),
            ],
        ),
        migrations.DeleteModel(
            name='ShoeColorSizeInventory',
        ),
    ]
