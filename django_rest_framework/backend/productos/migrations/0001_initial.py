# Generated by Django 4.0.6 on 2022-07-08 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('precio', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
            ],
        ),
    ]