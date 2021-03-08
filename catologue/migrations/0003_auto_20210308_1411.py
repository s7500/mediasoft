# Generated by Django 3.1.7 on 2021-03-08 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catologue', '0002_remove_product_feature'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='category_name',
        ),
        migrations.RenameField(
            model_name='manufacturer',
            old_name='name',
            new_name='manufacturer_name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='product_name',
        ),
        migrations.RenameField(
            model_name='subcategory',
            old_name='name',
            new_name='subcategory_name',
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catologue.subcategory'),
        ),
    ]
