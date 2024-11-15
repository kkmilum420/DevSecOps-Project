from django.db import models

# Create your models here.
class vehicleSearchRequest(models.Model):
    orderType = models.CharField(max_length=20,blank=True,default='')
    orderNo = models.CharField(max_length=9,blank=True,default='')
    busarea = models.CharField(max_length=10,blank=True,default='')
    modelId = models.CharField(max_length=20,blank=True,default='')
    chassisNo = models.CharField(max_length=10,blank=True,default='')
    vin = models.CharField(max_length=20,blank=True,default='')
    requestedDeliveryDate = models.CharField(max_length=10,blank=True,default='')
    deliveryLocation = models.CharField(max_length=20,blank=True,default='')
    orderStatus = models.CharField(max_length=15,blank=True,default='')
    actaulDeliveryDate = models.CharField(max_length=10,blank=True,default='')
    requestedBy = models.CharField(max_length=20,blank=True,default='')
    lastOrderNo = models.CharField(max_length=9,blank=True,default='')

class vehicleSearchResponse(models.Model):
    #orderNo = models.IntegerField(default=0)
    orderNo = models.CharField(max_length=9)
    busarea = models.CharField(max_length=10)
    modelId = models.CharField(max_length=20)
    orderType = models.CharField(max_length=20)
    chassisNo = models.CharField(max_length=10)
    vin = models.CharField(max_length=20)
    #requestedDeliveryDate = models.DateField(null=True)
    requestedDeliveryDate = models.CharField(max_length=10,default='')
    deliveryLocation = models.CharField(max_length=20)
    #orderQty = models.IntegerField(default=0)
    orderQty = models.CharField(max_length=10)
    #orderTotalCost = models.DecimalField(max_digits=15,decimal_places=2)
    orderTotalCost = models.CharField(max_length=18)
    orderStatus = models.CharField(max_length=15)
    actaulDeliveryDate = models.CharField(max_length=10,null=True)
    requestedBy = models.CharField(max_length=20)
    updatedBy = models.CharField(max_length=20)
    orderCreationTimestamp = models.CharField(max_length=10,null=True)
    updateTimestamp = models.CharField(max_length=9)