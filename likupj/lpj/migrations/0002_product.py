# Generated by Django 3.2.8 on 2021-11-19 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lpj', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=500)),
                ('product_date', models.DateField()),
            ],
        ),
    ]