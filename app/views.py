from django.shortcuts import render
from django.http import HttpResponse
from django.forms.models import model_to_dict
import json
from .models import Banks

# Create your views here.
def branch_details(request, ifsc):
    if (request.method == "GET"):
        a = Banks.objects.filter(ifsc=ifsc).values().first()
        if (a is None):
            return HttpRespone("resource not found", status=404)
        return HttpResponse(json.dumps(a))
    else:
        return HttpResponse("invalid method", 400)

def all_branches(request, bank_name, city):
    if (request.method == "GET"):
        a = Banks.objects.filter(city=city, bank_name=bank_name).values()
        if (a.count() == 0):
            return HttpRespone("resource not found", status=404)
        return HttpResponse(json.dumps(list(a)))
    else:
        HttpResponse("invalid method", status=400)