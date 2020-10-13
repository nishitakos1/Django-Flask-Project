from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'MainApp/index.html')

def about(request):
    return render(request,'MainApp/about.html')

def contact(request):
    return render(request,'MainApp/contact.html')

def productview(request):
    return render(request,'MainApp/product.html')

def training(request):
    return render(request,'MainApp/trainingpages.html')

def rblog(request):
    return render(request,'MainApp/Robotics(blogs).html')

def ablog(request):
    return render(request,'MainApp/AI(blog).html')

def weblog(request):
    return render(request,'MainApp/web(blog).html')

def emblog(request):
    return render(request,'MainApp/Embedded.html')

def pcblog(request):
    return render(request,'MainApp/PCB.html')

def dblog(request):
    return render(request,'MainApp/3D.html')

def stblog(request):
    return render(request,'MainApp/STEM.html')

def smablog(request):
    return render(request,'MainApp/Smart.html')

def roblog(request):
    return render(request,'MainApp/Robotic.html')

def mablog(request):
    return render(request,'MainApp/machinelearning.html')

def chatblog(request):
    return render(request,'MainApp/chatbot.html')

def clasblog(request):
    return render(request,'MainApp/cluster.html')

def ecomblog(request):
    return render(request,'MainApp/E-commerce_development.html')

def healthblog(request):
    return render(request,'MainApp/healthcare.html')

def imgblog(request):
    return render(request,'MainApp/imagerecongnition.html')

def inblog(request):
    return render(request,'MainApp/Intranetsolution.html')

def mobblog(request):
    return render(request,'MainApp/mobile applicationdevelopment.html')

def nlblog(request):
    return render(request,'MainApp/NLP.html')

def pyblog(request):
    return render(request,'MainApp/Python.html')

def selblog(request):
    return render(request,'MainApp/salesforcesystem.html')

def seblog(request):
    return render(request,'MainApp/SEO.html')

def sofblog(request):
    return render(request,'MainApp/Sofware_development.html')

def webblog(request):
    return render(request,'MainApp/web(blog).html')

