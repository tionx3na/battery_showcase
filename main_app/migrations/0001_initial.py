# Generated by Django 3.1.3 on 2020-12-03 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batterymodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warranty', models.CharField(max_length=10)),
                ('segment', models.CharField(choices=[('PC', 'PC'), ('CV', 'CV'), ('TR', 'TR'), ('OW', 'OHW')], max_length=2)),
                ('nomenclature', models.CharField(max_length=50)),
                ('capacity_C5', models.IntegerField()),
                ('capacity_C20', models.IntegerField()),
                ('reserve_capacity', models.IntegerField()),
                ('CCA', models.IntegerField()),
                ('length', models.IntegerField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('BH_type', models.CharField(max_length=10)),
                ('cell_layout', models.CharField(max_length=20)),
                ('model_pic', models.ImageField(null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'Battery Model',
                'verbose_name_plural': 'Battery Models',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Batteryrange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('range_name', models.CharField(max_length=10)),
                ('technology', models.CharField(max_length=200)),
                ('service_life', models.IntegerField()),
                ('cold_start_perf', models.IntegerField()),
                ('deep_cylce_resist', models.IntegerField()),
                ('no_of_electrical_consumers', models.IntegerField()),
                ('suitability_of_short_dist', models.IntegerField()),
                ('maintenance', models.CharField(choices=[('MF', 'Maintenance Free'), ('NF', 'Not Maintenance Free')], max_length=2)),
                ('installation_inside_vehicle', models.BooleanField(default=True)),
                ('installation_angle', models.IntegerField(default=0)),
                ('warranty_duration', models.IntegerField()),
                ('range_pic', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Battery Range',
                'verbose_name_plural': 'Battery Ranges',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Compatability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_class_name', models.CharField(max_length=10)),
                ('OEM', models.CharField(max_length=20)),
                ('vehicle_models', models.CharField(max_length=200)),
                ('model_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.batterymodel')),
                ('range_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.batteryrange')),
            ],
            options={
                'verbose_name': 'Compatibility',
                'verbose_name_plural': 'Compatibilities',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='batterymodel',
            name='range_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main_app.batteryrange'),
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_3_wheeler', models.BooleanField(default=False)),
                ('is_small_car', models.BooleanField(default=False)),
                ('is_large_car', models.BooleanField(default=False)),
                ('is_xtra_small_car', models.BooleanField(default=False)),
                ('is_small_van', models.BooleanField(default=False)),
                ('is_truck', models.BooleanField(default=False)),
                ('is_bus', models.BooleanField(default=False)),
                ('is_tractor', models.BooleanField(default=False)),
                ('is_JCB', models.BooleanField(default=False)),
                ('is_construction_vehicle', models.BooleanField(default=False)),
                ('is_bike', models.BooleanField(default=False)),
                ('is_scooter', models.BooleanField(default=False)),
                ('range_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main_app.batteryrange')),
            ],
            options={
                'verbose_name': 'Application',
                'verbose_name_plural': 'Applications',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Advantage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adv1_head', models.CharField(blank=True, max_length=200)),
                ('adv1_desc', models.CharField(blank=True, max_length=200)),
                ('adv2_head', models.CharField(blank=True, max_length=200)),
                ('adv2_desc', models.CharField(blank=True, max_length=200)),
                ('adv3_head', models.CharField(blank=True, max_length=200)),
                ('adv3_desc', models.CharField(blank=True, max_length=200)),
                ('adv4_head', models.CharField(blank=True, max_length=200)),
                ('adv4_desc', models.CharField(blank=True, max_length=200)),
                ('adv5_head', models.CharField(blank=True, max_length=200)),
                ('adv5_desc', models.CharField(blank=True, max_length=200)),
                ('adv6_head', models.CharField(blank=True, max_length=200)),
                ('adv6_desc', models.CharField(blank=True, max_length=200)),
                ('range_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main_app.batteryrange')),
            ],
            options={
                'verbose_name': 'Advantage',
                'verbose_name_plural': 'Advantages',
                'db_table': '',
                'managed': True,
            },
        ),
    ]