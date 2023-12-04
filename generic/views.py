from django.shortcuts import render

# Create your views here.
def chamu(request):
    return render(request,'chamu.html')

def sam(request):
    return render(request,'sam.html')