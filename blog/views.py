from django.shortcuts import render, HttpResponse

# Create your views here.
def blogHome(request): 
    # return HttpResponse('This is  blog home. We will keep all blog posts here')
    return render(request,'blog/blogHome.html')

def blogPost(request, slug): 
    # return HttpResponse(f'This is blogPost : {slug}')
    return render(request,'blog/blogPost.html')