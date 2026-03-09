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

def rajshahi(request):
    weather = {
        'location' : 'Rajshahi',
        'temperature' : 10,
        'condition' : 'Cloudy',
    }
    forcast = [ 'Sunny', 'rainy', 'cloudy', 'stormy', 'snowy', 'Cool' ]
    return render(request, 'day2/rajshahi.html', { 'weather' : weather, 'forcast' : forcast })