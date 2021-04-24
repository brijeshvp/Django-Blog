from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse('This is home')
    return render(request,'home/home.html')

def about(request):
    # return HttpResponse('This is about')
    return render(request,'home/about.html')


def contact(request):
    # return HttpResponse('This is contact')
    return render(request,'home/contact.html')