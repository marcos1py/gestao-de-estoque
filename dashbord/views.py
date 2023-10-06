from django.shortcuts import render

# Create your views here.
def index(request):
    
    context = {"produto":"Agua"}
    return render(request, 'dashbord.html',context)