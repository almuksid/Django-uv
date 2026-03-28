# Study
## Sanitization users, validation user
- Sanitization => Never trust your users
- Validation => 
- django, 
- tailwind css -> tailwind.config.js amd also install tailwind css intelegence extention inside vs code,
- decorators
- extends 


# Day1. What is uv and what is django & elplore django project and app
uv is alternatice for pip 
- https://docs.astral.sh/uv/getting-started/installation/
*open powershell then run this cmd*
- powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
## 1. How to setup django using uv 
- uv init
- uv venv
- uv add django
- uv run django-admin startproject projectName . (.root dir)
- uv run django-admin startapp appName (day1)
- uv run python manage.py migrate
- uv run python manage.py createsuperuser
- uv run python manage.py runserver

## 02. Create a folder name "scripts" file name "myScripts.py"

- uv run python scripts/startappx.py myapp1
---
# Day2. using variable, if else, loop, context & a Project
## 1. Context Processore
- Create a  file name context_processore.py, then 
```django
def global_data(request):
    return {
        'title' : 'Day2 Weather App'
    }
```

```django
'context_processors': [
    'day2.context_processore.global_data',
],
```
```django
<h2>{{ title }}</h2>
```
---
## 2. if else & for loop
- views.py
```django
from django.shortcuts import render

# Create your views here.
def dhaka(request):
    weather = {
        'location' : 'Dhaka',
        'temperature' : 10,
        'condition' : 'Sunny',
    }
    forcast = [ 'Sunny', 'rainy', 'cloudy', 'stormy', 'snowy', 'Cool' ]
    return render(request, 'day2/dhaka.html', { 'weather' : weather, 'forcast' : forcast })
```

- dhaka.html

```django
    <h2>{{ title }}</h2>
    <p>Location: {{ weather.location }}</p>
    <p>Temperature: {{ weather.temperature }}°C</p>
    <p>Condition: 
        {% if weather.temperature > 30 %}
            Hot
        {% elif weather.temperature > 20 %}
            Moderate
        {% elif weather.temperature > 10 %}
            Cool
        {% else %}
            super cold
        {% endif %}
    </p>
    <ul>
        {% for item in forcast %}
            <li>{{ item }}</li>
        {% endfor %}
    </ul>
```

## 03. Complete a project 
---

# Day3. Static Assets load & alpinejs 
## 01. 
contact.html
```html
<form action = "{% url 'day3:submission_handler' %}" method="post">
    {% csrf_token %}    
    <div class="row">
        <div class="col-6">
        <div class="form-group">
            <label class="text-black" for="fname">First name</label>
            <input type="text" class="form-control" id="fname" name="fname">
        </div>
        </div>
        <div class="col-6">
        <div class="form-group">
            <label class="text-black" for="lname">Last name</label>
            <input type="text" class="form-control" id="lname" name="lname">
        </div>
        </div>
    </div>
    <div class="form-group">
        <label class="text-black" for="email">Email address</label>
        <input type="email" class="form-control" id="email" name="email">
    </div>

    <div class="form-group mb-5">
        <label class="text-black" for="message">Message</label>
        <textarea name="message" class="form-control" id="message" cols="30" rows="5"></textarea>
    </div>

    <button type="submit" class="btn btn-primary-hover-outline">Send Message</button>
</form>
```
views.py
```
from django.http import JsonResponse

def contact(request):
    return render(request, 'day3/contact.html')

def submission_handler(request):
    data  = {
        'first_name': request.POST.get('fname'),
        'last_name': request.POST.get('lname'),   
        'email': request.POST.get('email'),
        'message': request.POST.get('message'),
    }
    return JsonResponse(data)
```
urls.py
```
app_name = 'day3'

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('submission_handler/', views.submission_handler, name='submission_handler'),
]
```
## 02. Success messages send 
contact.html
```django
{% if messages %}
      <div class="container mt-4">
        {% for message in messages %}
          <div class="alert alert-{{ message.tags }}" role="alert">
            {{ message }}
          </div>
        {% endfor %}
      </div>
    {% endif %}

```
views.py
```django
messages.success(request, 'Your form has been submitted successfully!')
return redirect('day3:contact')
```
success.html
```django
<div class="container">
  <h2 style="width: 50%;"> Your message has been sent successfully! </h2>
</div>
<script>
    setTimeout(() => {
        location.href = "/day3/contact/"
    }, 2000);
</script>

```

- Hardcode: messages send successfully
```django
def contact(request):
    success = request.GET.get('success') == '1'
    return render(request, 'day3/contact.html', {'success': success})

def submission_handler(request):
    return redirect('http://127.0.0.1:8000/day3/contact/?success=1')
```
- contact.html
```html
<div>
    {% if success %}
        <p>Messages send successfully!</p>
    {%endif %}
</div>
```

# Day4. Django Views
## 1. GET, POST, PUT, PATCH, DELETE
- *GET* Used to fetch data from the server.
- *POST* Used to create a new resource on the server.
- *PUT* Used to update an existing resource by replacing it.
- *PATCH* Used to update specific fields of a resource.
- *DELETE* Used to delete a resource from the server.


## 2. Resource collection
- users/ GET, POST
- users/1 GET, PUT, PATCH, DELETE


## 3. views.py 
```django

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, require_GET, require_POST

@csrf_exempt
# @require_http_methods(['GET', 'POST'])
@require_POST

```

## 4. Views types:
### 1. Function Based View
```django
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods, require_GET, require_POST


# Create your views here.
def number(request, number):
    isEven = (number % 2 == 0)
    return render(request, 'day4/sample.html', {"n": number, "isEven":isEven})

@csrf_exempt
# @require_http_methods(['GET', 'POST'])
@require_POST
def record(request, name, age):
    return HttpResponse("My name is " + name + " and I am " + str(age) + " years old." +"   Method:" + request.method, {"name" : name, "age" : age})

```
### 2. Function-Based API View that fetches external data and returns JSON response
```django
from django.http import HttpResponse, JsonResponse, Http404
import requests


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
```
### 3. Class Based View
```django
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.views import View
from django.utils.decorators import method_decorator


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
```

## 5. 4O4 error

```django
from django.http import HttpResponse, JsonResponse, Http404

class UserDetailsView(View):
    def get(self, request, id):
        if(id > 20):
            raise Http404("User not existed")
        else:
            pass
        return JsonResponse({"messages": "Hi We are try to practice all of them"})
```
