# Generated by Django 3.1.3 on 2020-12-03 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compatability',
            name='vehicle_class',
            field=models.CharField(choices=[('TW', 'Three Wheeler'), ('SC', 'Small Car'), ('LC', 'Large Car'), ('XC', 'Extra Small Car'), ('TK', 'Truck'), ('BS', 'Bus'), ('TR', 'Tractor'), ('JB', 'JCB'), ('CV', 'Construction Vehicle'), ('BK', 'Bike'), ('SR', 'Scooter'), ('SM', 'Small van')], max_length=2),
        ),
    ]