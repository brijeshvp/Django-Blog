from django.shortcuts import render,HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User

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

def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your Account has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")