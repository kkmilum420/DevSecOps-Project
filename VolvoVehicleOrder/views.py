from django.shortcuts import render, redirect
from django import forms
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, HttpResponsePermanentRedirect
from django.forms import formset_factory, BaseFormSet
from django.urls import re_path 
from rest_framework_swagger.views import get_swagger_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import *
from .serializers import*

###
import requests
import json
from decimal import Decimal

###
from VolvoVehicleOrder.forms import vehicleSearchRequestf
from VolvoVehicleOrder.forms import vehicleSearchResponsef, modifyVehicleOrderf
from VolvoVehicleOrder.models import vehicleSearchRequest
from VolvoVehicleOrder.models import vehicleSearchResponse

### for Swagger openAPI generation
schema_view = get_swagger_view(title='Pastebin API')
urlpatterns = [
    re_path(r'^$', schema_view)
]

### JSON Encoder for Decimal Values
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            # Convert Decimal to string for JSON serialization
            return str(obj)
        return super().default(obj)
    
class updatevehicleSearchRequest:
    def __init__(self, rqstform):
        if not isinstance(rqstform, vehicleSearchRequestf):
            raise ValueError('Input form must be a vehicleSearchRequest form')
        self.rqstform = rqstform
    def updateRequest(self):
        if self.rqstform.is_valid():
            reqstmodel = vehicleSearchRequest(
                orderType=self.rqstform.cleaned_data["orderType"],
                orderNo=self.rqstform.cleaned_data["orderNo"],
                busarea=self.rqstform.cleaned_data["busarea"],
                modelId=self.rqstform.cleaned_data["modelId"],
                chassisNo=self.rqstform.cleaned_data["chassisNo"],
                vin=self.rqstform.cleaned_data["vin"],
                requestedDeliveryDate=self.rqstform.cleaned_data["requestedDeliveryDate"],
                deliveryLocation=self.rqstform.cleaned_data["deliveryLocation"],
                orderStatus=self.rqstform.cleaned_data["orderStatus"],
                actaulDeliveryDate=self.rqstform.cleaned_data["actaulDeliveryDate"],
                requestedBy=self.rqstform.cleaned_data["requestedBy"],
                lastOrderNo=self.rqstform.cleaned_data["lastOrderNo"],                
            )
            reqstmodel.save()
            return True
        return False
    
# Create your views here.
def searchAndDisplay(request):
    if request.method == 'POST':
        reqform = vehicleSearchRequestf(request.POST)
        # search_input = request.session.get("search_input",{})
        # print ('Search input during intit:', search_input)
        # if search_input:
        #     reqform = vehicleSearchRequestf(request.POST, initial=search_input) 
        # else:
        #    reqform = vehicleSearchRequestf(request.POST) 
        resform = vehicleSearchResponsef()
        resmod = vehicleSearchResponse.objects.all()
        resmod.delete()

        request_updater = updatevehicleSearchRequest(reqform)
        if request_updater.updateRequest():
            pass
        else:
            raise RuntimeError('Request Model didnot update')

        if reqform.is_valid():
            base_url = 'https://sd01.srv.volvo.com:8443/ref-ims-vehicleorder/v1/orders'
            headers = {
                "content-type":"application/json",
                "accept":"application/json",
                "Authorization":"Basic YTI5MzQ5MTp2b2x2bzAy"
            }

            body = {
                    "order-request": {
                        "request-search": {
                            "seacrh-order-type": "",
                            "search-order": "",
                            "search-business-area": "",
                            "search-model-id": "",
                            "search-chassis": "",
                            "search-vin": "",
                            "search-requested-delivery-date": "",
                            "search-delivery-location": "",
                            "search-status": "",
                            "search-actual-delivery-date": "",
                            "search-requested-by": "",
                            "search-last-order": ""
                            }
                        }
                    }
            
            #print ('Order No:', request.POST.get('orderNo'))
            #print('Request: ', reqform.cleaned_data)

            if reqform.cleaned_data["orderType"]:
                body["order-request"]["request-search"]["seacrh-order-type"] = reqform.cleaned_data["orderType"]
            else:
                body["order-request"]["request-search"]["seacrh-order-type"] = ""
            
            if reqform.cleaned_data["orderNo"]:
                body["order-request"]["request-search"]["search-order"] = reqform.cleaned_data["orderNo"]
            else:
                body["order-request"]["request-search"]["search-order"] = ""            

            if reqform.cleaned_data["busarea"]:
                body["order-request"]["request-search"]["search-business-area"] = reqform.cleaned_data["busarea"]
            else:
                body["order-request"]["request-search"]["search-business-area"] = ""
            
            if reqform.cleaned_data["modelId"]:
                body["order-request"]["request-search"]["search-model-id"] = reqform.cleaned_data["modelId"]
            else:
                body["order-request"]["request-search"]["search-model-id"] = ""

            if reqform.cleaned_data["chassisNo"]:
                body["order-request"]["request-search"]["search-chassis"] = reqform.cleaned_data["chassisNo"]
            else:
                body["order-request"]["request-search"]["search-chassis"] = ""

            if reqform.cleaned_data["vin"]:
                body["order-request"]["request-search"]["search-vin"] = reqform.cleaned_data["vin"]
            else:
                body["order-request"]["request-search"]["search-vin"] = ""
            
            if reqform.cleaned_data["requestedDeliveryDate"]:
                body["order-request"]["request-search"]["search-requested-delivery-date"] = reqform.cleaned_data["requestedDeliveryDate"]
            else:
                body["order-request"]["request-search"]["search-requested-delivery-date"] = ""

            if reqform.cleaned_data["deliveryLocation"]:
                body["order-request"]["request-search"]["search-delivery-location"] = reqform.cleaned_data["deliveryLocation"]
            else:
                body["order-request"]["request-search"]["search-delivery-location"] = ""

            if reqform.cleaned_data["orderStatus"]:
                body["order-request"]["request-search"]["search-status"] = reqform.cleaned_data["orderStatus"]
            else:
                body["order-request"]["request-search"]["search-status"] = ""

            if reqform.cleaned_data["actaulDeliveryDate"]:
                body["order-request"]["request-search"]["search-actual-delivery-date"] = reqform.cleaned_data["actaulDeliveryDate"]
            else:
                body["order-request"]["request-search"]["search-actual-delivery-date"] = ""

            if reqform.cleaned_data["requestedBy"]:
                body["order-request"]["request-search"]["search-requested-by"] = reqform.cleaned_data["requestedBy"]
            else:
                body["order-request"]["request-search"]["search-requested-by"] = ""
            
            if reqform.cleaned_data["lastOrderNo"]:
                body["order-request"]["request-search"]["search-last-order"] = reqform.cleaned_data["lastOrderNo"]
            else:
                body["order-request"]["request-search"]["search-last-order"] = ""

            response = requests.get(base_url,headers=headers,data=json.dumps(body),verify=False)

            if response.status_code == 200:
                response_json = response.json()
                try:
                    response_detail = response_json["order-response"]["response-search"]["search-data"]
                except:
                        resform = vehicleSearchResponsef()
                else:
                    for data in response_detail:
                        v_orderNo=data["search-order"]
                        v_busarea=data["search-business-area"]
                        v_modelId=data["search-model-id"]
                        v_orderType=data["search-order-type"]
                        v_chassisNo=data["search-chassis"]
                        v_vin=data["search-vin"]
                        v_requestedDeliveryDate=data["search-requested-delivery-date"]
                        v_deliveryLocation=data["search-requested-delivery-location"]
                        v_orderQty=data["search-order-quantity"]
                        v_orderTotalCost=data["search-order-total-cost"]
                        v_orderStatus=data["search-order-status"]
                        v_actaulDeliveryDate=data["search-actual-delivery-date"]
                        v_requestedBy=data["search-requested-by"]
                        v_updatedBy=data["search-update-By"]
                        v_orderCreationTimestamp=data["search-order-creation-timestamp"]
                        v_updateTimestamp=data["search-order-update-timestamp"]
                        
                        #print ('busarea:', v_busarea)

                        if (v_orderNo > 0):
                            response_commit = vehicleSearchResponse(orderNo=v_orderNo,
                                                                    busarea = v_busarea,
                                                                    modelId = v_modelId,
                                                                    orderType = v_orderType,
                                                                    chassisNo = v_chassisNo,
                                                                    vin = v_vin,
                                                                    requestedDeliveryDate = v_requestedDeliveryDate,
                                                                    deliveryLocation = v_deliveryLocation,
                                                                    orderQty = v_orderQty,
                                                                    orderTotalCost = v_orderTotalCost,
                                                                    orderStatus = v_orderStatus,
                                                                    actaulDeliveryDate = v_actaulDeliveryDate,
                                                                    requestedBy = v_requestedBy,
                                                                    updatedBy = v_updatedBy,
                                                                    orderCreationTimestamp = v_orderCreationTimestamp,
                                                                    updateTimestamp = v_updateTimestamp
                                                                    )
                            response_commit.save()
                    resform = vehicleSearchResponse.objects.all()
                    reqform = vehicleSearchRequestf(request.POST)
                response_code = response_json["order-response"]["response-search"]["search-response-code"]
                response_message = response_json["order-response"]["response-search"]["search-reason-code"]
            else:
                print('Request failed with status code:', response.status_code)
                response_code = response.status_code
                response_message = response.reason
#Storing the search inputs as session parameter
            request.session["search_input"] = {
                "srch_orderType":request.POST.get('orderType'),
                "srch_orderNo":request.POST.get('orderNo'),
                "srch_busarea":request.POST.get('busarea'),
                "srch_modelId":request.POST.get('modelId'),
                "srch_chassisNo":request.POST.get('chassisNo'),
                "srch_vin":request.POST.get('vin'),
                "srch_requestedDeliveryDate":request.POST.get('requestedDeliveryDate'),
                "srch_deliveryLocation":request.POST.get('deliveryLocation'),
                "srch_orderStatus":request.POST.get('orderStatus'),
                "srch_actaulDeliveryDate":request.POST.get('actaulDeliveryDate'),
                "srch_requestedBy":request.POST.get('requestedBy'),
                "srch_lastOrderNo":request.POST.get('lastOrderNo'),
            }        
            #print('Before Render Search input:', search_input)
            return render(request, 'VolvoVehicleOrder/searchAndDisplay.html',{"reqform":reqform,"resform":resform,
                                                                              "response_code":response_code, 
                                                                              "response_message":response_message,})
                                                                              #"search_input":search_input})
    else:
        request_data = vehicleSearchRequest.objects.all()
        request_data.delete()
        reqform = vehicleSearchRequestf()
        resform = vehicleSearchResponsef()        
        return render(request, 'VolvoVehicleOrder/searchAndDisplay.html',{"reqform":reqform})
    #return render(request, 'VolvoVehicleOrder/searchAndDisplay.html',{"reqform":reqform,"resform":resform})

def modifyVehicleOrder(request, orderNo):
    print ('Method:', request.method)
    if (request.method == 'POST'):
        print ('if order no:', orderNo)
        ordReqForm = modifyVehicleOrderf(request.POST)
        
        if ordReqForm.is_valid():
            base_url = 'https://sd01.srv.volvo.com:8443/ref-ims-vehicleorder/v1/oldorder/order-no/'
            headers = {
                "content-type":"application/json",
                "accept":"application/json",
                "Authorization":"Basic YTI5MzQ5MTpkZXZvcHMy"
            }
            update_url = base_url + orderNo 

            body = {
                    "order-request": {
                        "request-change": {
                            "change-order-quantity": 0,
                            "change-order-cost": 0,
                            "change-actual-delivery-date": "",
                            "change-status": ""
                            }
                        }
                    }

            if ordReqForm.cleaned_data["orderQty"]:
                body["order-request"]["request-change"]["change-order-quantity"] = ordReqForm.cleaned_data["orderQty"]
            else:
                body["order-request"]["request-change"]["change-order-quantity"] = ""
            
            if ordReqForm.cleaned_data["orderCost"]:
                body["order-request"]["request-change"]["change-order-cost"] = ordReqForm.cleaned_data["orderCost"]
            else:
                body["order-request"]["request-change"]["change-order-cost"] = 0            

            if ordReqForm.cleaned_data["actualDeliveryDate"]:
                body["order-request"]["request-change"]["change-actual-delivery-date"] = ordReqForm.cleaned_data["actualDeliveryDate"]
            else:
                body["order-request"]["request-change"]["change-actual-delivery-date"] = ""
            
            if ordReqForm.cleaned_data["orderStatus"]:
                body["order-request"]["request-change"]["change-status"] = ordReqForm.cleaned_data["orderStatus"]
            else:
                body["order-request"]["request-change"]["change-status"] = ""

            
            response = requests.put(update_url,headers=headers,data=json.dumps(body, cls=DecimalEncoder),verify=False)

            if response.status_code == 200:
               response_json = response.json()
               response_detail = response_json["order-response"]["response-change"]
               try:
                   ord = vehicleSearchResponse.objects.get(orderNo=orderNo)
               except vehicleSearchResponse.DoesNotExist:
                   print ('No records found for Order no:', orderNo)
               else:
                   updform = modifyVehicleOrderf(initial={
                       'orderNo':ord.orderNo,
                       'busarea':ord.busarea,
                       'modelId':ord.modelId,
                       'orderType':ord.orderType,
                       'chassisNo':ord.chassisNo,
                       'vin':ord.vin,
                       'actualDeliveryDate':ordReqForm.cleaned_data["actualDeliveryDate"],
                       'orderQty':ordReqForm.cleaned_data["orderQty"],
                       'orderCost':ordReqForm.cleaned_data["orderCost"],
                       'orderStatus':ordReqForm.cleaned_data["orderStatus"],
                       'message':response_detail["change-reason-code"]
                       })
            else:
                print('Request failed with status code:', response.status_code)
        else:
            print ('Update Form is invalid')
            print ('Form data:', ordReqForm)
    else:
        try:
            ord = vehicleSearchResponse.objects.get(orderNo=orderNo)
        except vehicleSearchResponse.DoesNotExist:
            print ('No records found for Order no:', orderNo)
        else:            
            cost = str(Decimal(ord.orderTotalCost)/int(ord.orderQty))
            updform = modifyVehicleOrderf(initial={
                'orderNo':ord.orderNo,
                'busarea':ord.busarea,
                'modelId':ord.modelId,
                'orderType':ord.orderType,
                'chassisNo':ord.chassisNo,
                'vin':ord.vin,
                'actualDeliveryDate':ord.actaulDeliveryDate,
                'orderQty':ord.orderQty,
                'orderCost':cost,
                'orderStatus':ord.orderStatus
            })
    return render(request, 'VolvoVehicleOrder/modifyVehicleOrder.html', {"form":updform})


def deleteVehicleOrder(request, orderNo):
    print ('Cancelling Process')
    if (request.method == 'GET'):
        reqform = vehicleSearchRequestf(request.POST)
        resform = vehicleSearchResponsef()
        base_url = 'https://sd01.srv.volvo.com:8443/ref-ims-vehicleorder/v1/archiveorder/order-no/'
        headers = {
            "content-type":"application/json",
            "accept":"application/json",
            "Authorization":"Basic YTI5MzQ5MTpkZXZvcHMy"
        }
        update_url = base_url + orderNo 
        response = requests.delete(update_url,headers=headers,verify=False)
        if response.status_code == 200:
            ord = vehicleSearchResponse.objects.get(orderNo=orderNo)
            ord.delete()
        else:
            print ('Request failed with status code:', response.status_code)
        return HttpResponsePermanentRedirect('/')
        #resform = vehicleSearchResponse.objects.all()
        #return render(request, 'VolvoVehicleOrder/searchAndDisplay.html',{"reqform":reqform,"resform":resform})
    