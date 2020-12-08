from django.db import models

# Create your models here.
MAINTAIN = (
    ('MF', 'Maintenance Free'),
    ('NF', 'Not Maintenance Free')
) # Category for Maintenance free or not

SEGMENT = (
    ('PC', 'PC'),
    ('CV', 'CV'),
    ('TR', 'TR'),
    ('OW', 'OHW'),
)

CLASS = (
    ('TW', 'Three Wheeler'),
    ('SC', 'Small Car'),
    ('LC', 'Large Car'),
    ('XC', 'Extra Small Car'),
    ('TK', 'Truck'),
    ('BS', 'Bus'),
    ('TR', 'Tractor'),
    ('JB', 'JCB'),
    ('CV', 'Construction Vehicle'),
    ('BK', 'Bike'),
    ('SR', 'Scooter'),
    ('SM', 'Small van')
)

BISC = (
    ('BK', 'Bike'),
    ('SC', 'Scooter')
)


class Batteryrange(models.Model):
    range_name = models.CharField(max_length=10, blank=False)
    technology = models.CharField(max_length=200, blank=False)
    service_life = models.IntegerField(blank=False)
    cold_start_perf = models.IntegerField(blank=False)
    deep_cylce_resist = models.IntegerField(blank=False)
    no_of_electrical_consumers = models.IntegerField(blank=False)
    suitability_of_short_dist = models.IntegerField(blank=False)
    maintenance = models.CharField(choices=MAINTAIN,max_length=2, blank=False)
    installation_inside_vehicle = models.BooleanField(default=True,blank=False)
    installation_angle = models.IntegerField(default=0,blank=False)
    warranty_duration = models.IntegerField(blank=False)
    range_pic = models.ImageField(blank=False)  # Profile picture of a battery from each ranges

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Battery Range'
        verbose_name_plural = 'Battery Ranges'

    def __str__(self):
        return self.range_name

    @property
    def imageURL(self):
        try:
            url = self.range_pic.url
        except:
            url = ''
        return url


class Application(models.Model):
    range_id = models.ForeignKey(Batteryrange, on_delete=models.CASCADE, default=0) # Foriegn Key
    is_3_wheeler =  models.BooleanField(default=False)
    is_small_car = models.BooleanField(default=False)
    is_large_car = models.BooleanField(default=False)
    is_xtra_small_car = models.BooleanField(default=False)
    is_small_van = models.BooleanField(default=False)
    is_truck = models.BooleanField(default=False)
    is_bus = models.BooleanField(default=False)
    is_tractor = models.BooleanField(default=False)
    is_JCB = models.BooleanField(default=False)
    is_construction_vehicle = models.BooleanField(default=False)
    is_bike = models.BooleanField(default=False)
    is_scooter = models.BooleanField(default=False)


    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Application'
        verbose_name_plural = 'Applications'


class Advantage(models.Model):
    range_id = models.ForeignKey(Batteryrange, on_delete=models.CASCADE, default=0) # Foriegn Key
    adv1_head = models.CharField(max_length=200, blank=True)
    adv1_desc = models.CharField(max_length=200, blank=True)
    adv2_head = models.CharField(max_length=200, blank=True)
    adv2_desc = models.CharField(max_length=200, blank=True)
    adv3_head = models.CharField(max_length=200, blank=True)
    adv3_desc = models.CharField(max_length=200, blank=True)
    adv4_head = models.CharField(max_length=200, blank=True)
    adv4_desc = models.CharField(max_length=200, blank=True)
    adv5_head = models.CharField(max_length=200, blank=True)
    adv5_desc = models.CharField(max_length=200, blank=True)
    adv6_head = models.CharField(max_length=200, blank=True)
    adv6_desc = models.CharField(max_length=200, blank=True)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Advantage'
        verbose_name_plural = 'Advantages'

class Batterymodel(models.Model):
    range_id = models.ForeignKey(Batteryrange,on_delete=models.CASCADE,default=0) # Foriegn Key
    part_number = models.CharField(max_length=20, blank=False,default=0)
    warranty = models.CharField(max_length=20, blank=False)
    segment = models.CharField(choices=SEGMENT, blank=False,max_length=2) # $ types of segments as of now
    nomenclature = models.CharField(max_length=50, blank=False)
    capacity_C5 = models.IntegerField(blank=False)
    capacity_C20 = models.IntegerField(blank=False)
    reserve_capacity = models.IntegerField(blank=False)
    CCA = models.IntegerField(blank=False)
    length = models.IntegerField(blank=False)
    width = models.IntegerField(blank=False)
    height = models.IntegerField(blank=False)
    weight = models.FloatField(blank=False)
    BH_type = models.CharField(max_length=10, blank=True)
    cell_layout = models.CharField(max_length=20, blank=False)
    model_pic = models.ImageField(null=True, blank=False)
    price = models.FloatField(default=0, blank=False)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Battery Model'
        verbose_name_plural = 'Battery Models'

    def __str__(self):
        return self.part_number

    @property
    def imageURL(self):
        try:
            url = self.model_pic.url
        except:
            url = ''
        return url


class Compatability(models.Model):
    range_id = models.ForeignKey(Batteryrange,on_delete=models.CASCADE) # Foriegn key from BatteryRanges
    model_id = models.ForeignKey(Batterymodel,on_delete=models.CASCADE) # Foriegn key from BatteryModels
    vehicle_class = models.CharField(choices=CLASS, max_length=2, blank=False)
    OEM = models.CharField(max_length=20, blank=False)
    vehicle_models = models.CharField(max_length=200, blank=False)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Compatibility'
        verbose_name_plural = 'Compatibilities'

    def __str__(self):
        return self.OEM


class Bikes(models.Model):
    range_id = models.ForeignKey(Batteryrange,on_delete=models.CASCADE) # Foriegn key from BatteryRanges
    model_id = models.CharField(max_length=20, blank=False,default=0)
    bike_pic = models.ImageField(blank=False)  # Profile picture of a battery from each ranges
    price = models.FloatField(default=0, blank=False)


    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Bike'
        verbose_name_plural = 'Bikes'

    def __str__(self):
        return self.model_id

    @property
    def imageURL(self):
        try:
            url = self.bike_pic.url
        except:
            url = ''
        return url

class Compatabilitybike(models.Model):
    bike_id = models.ForeignKey(Bikes,on_delete=models.CASCADE) # Foriegn key from Bikes
    OEM = models.CharField(max_length=20, blank=False)
    application = models.CharField(max_length=200, blank=False)
    C10 = models.FloatField(blank=False)
    battery_type = models.CharField(max_length=20, blank=False)
    bike_scooter = models.CharField(choices=BISC, max_length=2, blank=True)



    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Bike Compatability'
        verbose_name_plural = 'Bike compatabilities'

    def __str__(self):
        return self.OEM


class Amaronseries(models.Model):
    series = models.CharField(max_length=50, blank=False)
    capacity = models.IntegerField(blank=False)
    battery_type = models.CharField(max_length=50, blank=False)
    warranty = models.IntegerField(blank=False)
    usage = models.CharField(max_length=50, blank=False)
    voltage = models.IntegerField(blank=False)
    weight = models.FloatField(blank=False)
    technology = models.CharField(max_length=50, blank=False)
    variable_ranges = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=550, blank=False)
    price_range = models.CharField(max_length=50, blank=True)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Amaron Series'
        verbose_name_plural = 'Amaron Series'

    def __str__(self):
        return self.series


class Advantagesamaron(models.Model):
    series_id = models.ForeignKey(Amaronseries,on_delete=models.CASCADE) # Foriegn key from Amaronseries
    adv1 = models.CharField(max_length=200, blank=True)
    adv2 = models.CharField(max_length=200, blank=True)
    adv3 = models.CharField(max_length=200, blank=True)
    adv4 = models.CharField(max_length=200, blank=True)
    adv5 = models.CharField(max_length=200, blank=True)
    adv6 = models.CharField(max_length=200, blank=True)
    adv7 = models.CharField(max_length=200, blank=True)
    adv8 = models.CharField(max_length=200, blank=True)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Amaron Advantage'
        verbose_name_plural = 'Amaron Advantages'



class Amaronmodels(models.Model):
    series_id = models.ForeignKey(Amaronseries,on_delete=models.CASCADE) # Foriegn key from Amaronseries
    type = models.CharField(max_length=20, blank=True)
    item = models.CharField(max_length=100, blank=True)
    capacity = models.IntegerField(blank=False)
    warranty = models.IntegerField(blank=False)
    price = models.IntegerField(blank=False)


    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Amaron models'
        verbose_name_plural = 'Amaron models'

    def __str__(self):
        return self.item










