from django.core import validators
from django import forms
from .models import vehicleSearchRequest, vehicleSearchResponse

class vehicleSearchRequestf(forms.ModelForm):
    class Meta:
        model = vehicleSearchRequest
        fields = ['orderType', 'orderNo', 'busarea', 'modelId', 'chassisNo', 'vin',
                    'requestedDeliveryDate', 'deliveryLocation', 'orderStatus', 'actaulDeliveryDate',
                    'requestedBy', 'lastOrderNo']
    
        widgets = {
            'orderType':forms.TextInput(attrs={'class':'form-control'}),
            'orderNo':forms.TextInput(attrs={'class':'form-control'}),
            'busarea':forms.TextInput(attrs={'class':'form-control'}),
            'modelId':forms.TextInput(attrs={'class':'form-control'}),
            'chassisNo':forms.TextInput(attrs={'class':'form-control'}),
            'vin':forms.TextInput(attrs={'class':'form-control'}),
            'requestedDeliveryDate':forms.TextInput(attrs={'class':'form-control'}),
            'deliveryLocation':forms.TextInput(attrs={'class':'form-control'}),
            'orderStatus':forms.TextInput(attrs={'class':'form-control'}),
            'actaulDeliveryDate':forms.TextInput(attrs={'class':'form-control'}),
            'requestedBy':forms.TextInput(attrs={'class':'form-control'}),
            'lastOrderNo':forms.TextInput(attrs={'class':'form-control'})
        }
        

class vehicleSearchResponsef(forms.ModelForm):
    class Meta:
        model = vehicleSearchResponse
        fields = ['orderNo', 'busarea', 'modelId', 'orderType', 'chassisNo', 'vin',
                    'requestedDeliveryDate', 'deliveryLocation','orderQty','orderTotalCost', 'orderStatus', 
                    'actaulDeliveryDate','requestedBy', 'updatedBy','orderCreationTimestamp','updateTimestamp']
        widgets = {
                    'orderNo':forms.NumberInput(attrs={'class':'form-control'}),
                    'busarea':forms.TextInput(attrs={'class':'form-control'}),
                    'modelId':forms.TextInput(attrs={'class':'form-control'}),
                    'orderType':forms.TextInput(attrs={'class':'form-control'}),
                    'chassisNo':forms.TextInput(attrs={'class':'form-control'}),
                    'vin':forms.TextInput(attrs={'class':'form-control'}),
                    'requestedDeliveryDate':forms.TextInput(attrs={'class':'form-control'}),
                    'deliveryLocation':forms.TextInput(attrs={'class':'form-control'}),
                    'orderQty':forms.NumberInput(attrs={'class':'form-control'}),
                    'orderTotalCost':forms.NumberInput(attrs={'class':'form-control'}),
                    'orderStatus':forms.TextInput(attrs={'class':'form-control'}),
                    'actaulDeliveryDate':forms.TextInput(attrs={'class':'form-control'}),
                    'requestedBy':forms.TextInput(attrs={'class':'form-control'}),
                    'updatedBy':forms.TextInput(attrs={'class':'form-control'}),
                    'orderCreationTimestamp':forms.TextInput(attrs={'class':'form-control'}),
                    'updateTimestamp':forms.TextInput(attrs={'class':'form-control'}),
                }

class modifyVehicleOrderf(forms.Form):
    orderNo=forms.CharField(max_length=9,disabled=True,required=False,
                            widget=forms.TextInput(attrs={'class':'form-control'}))
    busarea = forms.CharField(max_length=10,disabled=True,required=False,
                              widget=forms.TextInput(attrs={'class':'form-control'}))
    modelId = forms.CharField(max_length=20,disabled=True,required=False,
                              widget=forms.TextInput(attrs={'class':'form-control'}))
    orderType = forms.CharField(max_length=20,disabled=True,required=False,
                                widget=forms.TextInput(attrs={'class':'form-control'}))
    chassisNo = forms.CharField(max_length=10,disabled=True,required=False,
                                widget=forms.TextInput(attrs={'class':'form-control'}))
    vin = forms.CharField(max_length=20,disabled=True,required=False,
                          widget=forms.TextInput(attrs={'class':'form-control'}))
    actualDeliveryDate = forms.CharField(max_length=10,required=False,
                                         widget=forms.TextInput(attrs={'class':'form-control'}))
    orderQty = forms.IntegerField(required=False,
                                  widget=forms.TextInput(attrs={'class':'form-control'}))
    orderCost = forms.DecimalField(max_digits=15,decimal_places=2,required=False,
                                   widget=forms.TextInput(attrs={'class':'form-control'}))
    orderStatus = forms.CharField(max_length=15,required=False,
                                  widget=forms.TextInput(attrs={'class':'form-control'}))
    message = forms.CharField(max_length=70,disabled=True,required=False,
                              widget=forms.TextInput(attrs={'class':'alert alert-success'}))