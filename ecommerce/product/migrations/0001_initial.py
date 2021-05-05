# Generated by Django 3.2.1 on 2021-05-05 06:56

from django.db import migrations, models


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
                ('price', models.PositiveIntegerField()),
                ('size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], default='S', max_length=2)),
                ('description', models.TextField()),
                ('images', models.ImageField(upload_to='static')),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]