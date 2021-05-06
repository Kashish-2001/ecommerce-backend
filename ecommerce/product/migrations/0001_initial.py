# Generated by Django 3.2.1 on 2021-05-06 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('actual_price', models.PositiveIntegerField()),
                ('selling_price', models.PositiveIntegerField(blank=True, null=True)),
                ('brand', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('Women', 'Women'), ('Men', 'Men'), ('Unisex', 'Unisex'), ('Kids', 'Kids')], max_length=50)),
                ('sub_category', models.CharField(choices=[('T-shirt', 'T-shirt'), ('Shirt', 'Shirt'), ('Jeans', 'Jeans'), ('Accessories', 'Accessories')], max_length=50)),
                ('description', models.TextField()),
                ('thumbnail', models.ImageField(default=None, upload_to='thumbnail/')),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='product_images/')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='image', to='product.product')),
            ],
        ),
    ]
