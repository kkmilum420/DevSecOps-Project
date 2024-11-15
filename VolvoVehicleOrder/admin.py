from django.contrib import admin
from .models import vehicleSearchRequest, vehicleSearchResponse

# Register your models here.
@admin.register(vehicleSearchRequest)
class vehicleSearchRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'orderType', 'orderNo', 'busarea', 'modelId', 'chassisNo', 'vin',
                    'requestedDeliveryDate', 'deliveryLocation', 'orderStatus', 'actaulDeliveryDate',
                    'requestedBy', 'lastOrderNo') 

@admin.register(vehicleSearchResponse)
class vehicleSearchResponseAdmin(admin.ModelAdmin):
    list_display = ('id', 'orderNo', 'busarea', 'modelId', 'orderType', 'chassisNo', 'vin',
                    'requestedDeliveryDate', 'deliveryLocation', 'orderQty', 'orderTotalCost', 
                    'orderStatus', 'actaulDeliveryDate', 'requestedBy', 'updatedBy', 
                    'orderCreationTimestamp', 'updateTimestamp') 