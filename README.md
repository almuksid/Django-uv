# Day1. 
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
# Day2. 
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