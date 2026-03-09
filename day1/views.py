from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, World!")

def json_view(request):
    data = {
        'message': 'Hello, World!',
        'status': 'success'
    }
    return JsonResponse(data)

def dhaka(request):
    weather = {
        'location' : 'Dhaka',
        'temperature': '18 degree', 
        'conditon': 'Cold'
    }
    return JsonResponse(weather)

def rajshahi(request):
    weather = {
        'location' : 'rajshahi',
        'temperature' : '12 degree',
        'condition' : 'Super cold'
    }
    return JsonResponse(weather)
