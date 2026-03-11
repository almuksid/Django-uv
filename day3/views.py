from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib import messages
# Create your views here.

def contact(request):
    return render(request, 'day3/contact.html')

def submission_handler(request):
    data  = {
        'first_name': request.POST.get('fname'),
        'last_name': request.POST.get('lname'),   
        'email': request.POST.get('email'),
        'message': request.POST.get('message'),
    }
    # return JsonResponse(data)

    # messages.success(request, 'Your form has been submitted successfully!')
    # return redirect('day3:contact')
    
    return render(request, 'day3/messages.html')
