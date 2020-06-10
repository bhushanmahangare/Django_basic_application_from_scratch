from django.shortcuts import render
from .models import Destination

# Create your views here.

def index(request):

    dest1 = Destination()   #create destination object
    dest1.name = "Mumbai"
    dest1.desc = "The city is newver "

    return render(request,'index.html',{'dest1':dest1} )


def about(request):
    return render(request,'about.html')