from django.db import models

# Create your models here.
class Banks(models.Model):

    class Meta:
        db_table = 'banks'

    ifsc = models.CharField(max_length=12, blank=True, default=None)
    bank_id = models.IntegerField(blank=True, default=None)
    branch = models.CharField(max_length=80, blank=True, default=None)
    address = models.CharField(max_length=200, blank=True, default=None)
    city = models.CharField(max_length=50, blank=True, default=None)
    district = models.CharField(max_length=50, blank=True, default=None)
    state = models.CharField(max_length=26, blank=True, default=None)
    bank_name = models.CharField(max_length=100, blank=True, default=None)

    
