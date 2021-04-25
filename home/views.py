from django.shortcuts import render,HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    # return HttpResponse('This is home')
    return render(request,'home/home.html')

def about(request):
    # return HttpResponse('This is about')
    return render(request,'home/about.html')

def contact(request):
    if request.method=="POST":  #whenever submit is clicked on contact form
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        contact=Contact(name=name, email=email, phone=phone, content=content)   #creating object of Contact class and passing parameters(constructor)
        contact.save()  #saving Contact object in database
    return render(request, "home/contact.html")
