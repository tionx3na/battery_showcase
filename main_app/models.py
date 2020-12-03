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


class BatteryRange(models.Model):
    range_id = models.AutoField(primary_key=True, default=0) # Primary Key
    range_name = models.CharField(max_length=10,null=False)
    technology = models.CharField(max_length=200, null=False)
    service_life = models.IntegerField(null=False,blank=False)
    cold_start_perf = models.IntegerField(null=False,blank=False)
    deep_cylce_resist = models.IntegerField(null=False,blank=False)
    no_of_electrical_consumers = models.IntegerField(null=False,blank=False)
    suitability_of_short_dist = models.IntegerField(null=False,blank=False)
    maintenance = models.CharField(choices=MAINTAIN, null=False, max_length=2)
    installation_inside_vehicle = models.BooleanField(default=True,null=True,blank=False)
    installation_angle = models.IntegerField(null=False,default=0,blank=False)
    warranty_duration = models.IntegerField(null=False,blank=False)
    range_pic = models.ImageField(null=True, blank=True)  # Profile picture of a battery from each ranges

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
    range_id = models.ForeignKey(BatteryRange, on_delete=models.CASCADE, default=0) # Foriegn Key
    application_id = models.AutoField(primary_key=True, default=0)  # Primary key
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

    def __str__(self):
        return self.range_name

class Advantage(models.Model):
    range_id = models.ForeignKey(BatteryRange, on_delete=models.CASCADE,default=0) # Foriegn Key
    advantage_id = models.AutoField(primary_key=True, default=0) # Primary key
    adv1_head = models.CharField(max_length=200, null=True)
    adv1_desc = models.CharField(max_length=200, null=True)
    adv2_head = models.CharField(max_length=200, null=True)
    adv2_desc = models.CharField(max_length=200, null=True)
    adv3_head = models.CharField(max_length=200, null=True)
    adv3_desc = models.CharField(max_length=200, null=True)
    adv4_head = models.CharField(max_length=200, null=True)
    adv4_desc = models.CharField(max_length=200, null=True)
    adv5_head = models.CharField(max_length=200, null=True)
    adv5_desc = models.CharField(max_length=200, null=True)
    adv6_head = models.CharField(max_length=200, null=True)
    adv6_desc = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Advantage'
        verbose_name_plural = 'Advantages'

    def __str__(self):
        return self.range_id




class BatteryModel(models.Model):
    range_id = models.ForeignKey(BatteryRange,on_delete=models.CASCADE,default=0) # Foriegn Key
    part_number = models.CharField(max_length=20,primary_key=True,unique=True) # Primary Key
    warranty = models.CharField(max_length=10, null=False)
    segment = models.CharField(choices=SEGMENT, null=False, max_length=2) # $ types of segments as of now
    nomenclature = models.CharField(max_length=50, null=False)
    capacity_C5 = models.IntegerField(null=False,blank=False)
    capacity_C20 = models.IntegerField(null=False,blank=False)
    reserve_capacity = models.IntegerField(null=False,blank=False)
    CCA = models.IntegerField(null=False,blank=False)
    length = models.IntegerField(null=False,blank=False)
    width = models.IntegerField(null=False,blank=False)
    height = models.IntegerField(null=False,blank=False)
    weight = models.IntegerField(null=False,blank=False)
    BH_type = models.CharField(max_length=10, null=False)
    cell_layout = models.CharField(max_length=20, null=False)
    model_pic = models.ImageField(null=True, blank=True)

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
            url = self.range_pic.url
        except:
            url = ''
        return url


class Compatability(models.Model):
    compatability_id = models.AutoField(primary_key=True, default=0) # Primary key
    range_id = models.ForeignKey(BatteryRange,on_delete=models.CASCADE) # Foriegn key from BatteryRanges
    model_id = models.ForeignKey(BatteryModel,on_delete=models.CASCADE) # Foriegn key from BatteryModels
    vehicle_class_name = models.CharField(max_length=10, null=False)
    OEM = models.CharField(max_length=20, null=False)
    vehicle_models = models.CharField(max_length=200, null=False)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Compatibility'
        verbose_name_plural = 'Compatibilities'

    def __str__(self):
        return self.vehicle_class_name
