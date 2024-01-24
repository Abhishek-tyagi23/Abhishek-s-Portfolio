from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    # return HttpResponse("This is a home page")
    
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def project(request):
    return render(request, 'project.html')

def contact(request):
    if request.method =="POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        subject= request.POST.get('subject')
        text = request.POST.get('text')
        contact=Contact(name=name,phone=phone,email=email,subject=subject,text=text,date=datetime.today())
        contact.save()
        messages.success(request,"Your message has been Success send!")
    return render(request, 'contact.html')

