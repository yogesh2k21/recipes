from django.shortcuts import render

# Create your views here.
def home(request):
    # allposts=Post.objects.all()
    # context={'content':allposts}
    return render(request,'app/home.html')