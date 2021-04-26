from django.shortcuts import render,HttpResponse
from home.models import Contact
from django.contrib import messages
from blog.models import Post

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
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)   #creating object of Contact class and passing parameters(constructor)
            contact.save()  #saving Contact object in database
            messages.success(request, "Your message has been sent successfully! We will surely respond you soon.")
    return render(request, "home/contact.html")

def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPosts=Post.objects.none()
    else:
        allPostsTitle= Post.objects.filter(title__icontains=query)  #search in blogtitle
        allPostsAuthor= Post.objects.filter(author__icontains=query)    #search in blogauthor
        allPostsContent =Post.objects.filter(content__icontains=query)  #search in blogcontent
        allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor)
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)