# Generated by Django 3.2.7 on 2023-07-25 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agenciaApp', '0002_aerolinea_remove_account_balance_vuelo_venta_reserva_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='Categorias')),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='Productos')),
                ('descripción', models.CharField(max_length=50, verbose_name='descripción')),
                ('precio', models.FloatField()),
                ('foto', models.ImageField(upload_to='images/')),
                ('cantidad', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Subcategorias',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='subcategoria')),
                ('descripción', models.CharField(max_length=50, verbose_name='descripción')),
                ('nombreCategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agenciaApp.categorias')),
            ],
        ),
        migrations.RemoveField(
            model_name='factura',
            name='user',
        ),
        migrations.RemoveField(
            model_name='factura',
            name='venta',
        ),
        migrations.RemoveField(
            model_name='reserva',
            name='user',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='vuelo',
        ),
        migrations.RemoveField(
            model_name='vuelo',
            name='aerolinea',
        ),
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.DeleteModel(
            name='Aerolinea',
        ),
        migrations.DeleteModel(
            name='Factura',
        ),
        migrations.DeleteModel(
            name='Reserva',
        ),
        migrations.DeleteModel(
            name='Venta',
        ),
        migrations.DeleteModel(
            name='Vuelo',
        ),
        migrations.AddField(
            model_name='productos',
            name='subcategoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agenciaApp.subcategorias'),
        ),
    ]
