from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'day2project/index.html')

def services(request):
    return render(request, 'day2project/services.html')

def contact(request):
    return render(request, 'day2project/contact.html')

def shop(request):
    return render(request, 'day2project/shop.html')
 
def about(request):
    return render(request, 'day2project/about.html')

def blog(request):
    return render(request, 'day2project/blog.html')

def cart(request):
    return render(request, 'day2project/cart.html')

def checkout(request):
    return render(request, 'day2project/checkout.html')

def thankyou(request):
    return render(request, 'day2project/thankyou.html')