# Generated by Django 3.2.4 on 2021-06-12 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='locations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locationname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='productCategoy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Categoryname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='shopDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopOwner', models.CharField(max_length=40)),
                ('shopName', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=50)),
                ('shopLocation', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Shop.locations')),
            ],
        ),
        migrations.CreateModel(
            name='productShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=40)),
                ('productDescription', models.TextField()),
                ('productCategory', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Shop.productcategoy')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.shopdetail')),
            ],
        ),
    ]
