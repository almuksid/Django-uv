from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.views import View
from django.utils.decorators import method_decorator
import requests

# Create your views here.
def number(request, number):
    isEven = (number % 2 == 0)
    return render(request, 'day4/sample.html', {"n": number, "isEven":isEven})

@csrf_exempt
# @require_http_methods(['GET', 'POST'])
@require_POST
def record(request, name, age):
    return HttpResponse("My name is " + name + " and I am " + str(age) + " years old." +"   Method:" + request.method, {"name" : name, "age" : age})

def json_users(request):
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        data = response.json()
    except request.RequestException as e:
        response = requests.get("https://jsonplaceholder.typicode.com/posts")

    return JsonResponse(data, safe=False)

def json_single_users(request, userId):
    try:
        response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{userId}")
        data = response.json()
    except request.RequestException as e:
        response = requests.get("https://jsonplaceholder.typicode.com/posts")

    return JsonResponse(data, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class UserViews(View):
    def get(self, request):
        return JsonResponse({"message": "Hi this is the Al Muksid"})
    
    def post(self, request):
        return JsonResponse({"message": "Hi this is the Al Muksid"})
    
    def put(self, request):
        return JsonResponse({"message": "Hi this is the Al Muksid"})
    
    def patch(self, request):
        return JsonResponse({"message": "Hi this is the Al Muksid"})
    
    def delete(self, request):
        return JsonResponse({"message": "Hi this is the Al Muksid"})    
    
@method_decorator(csrf_exempt, name="dispatch")
class UserDetailsView(View):
    def get(self, request, id):
        if(id > 20):
            raise Http404("User not existed")
        else:
            pass
        return JsonResponse({"messages": "Hi We are try to practice all of them"})
    
    def put(self, request, id):
        return JsonResponse({"messages": "Hi We are try to practice all of them"})
    
    def patch(self, request, id):
        return JsonResponse({"messages": "Hi We are try to practice all of them"})
    
    def delete(self, request, id):
        return JsonResponse({"messages": "Hi We are try to practice all of them"})
