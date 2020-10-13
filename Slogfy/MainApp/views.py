from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
<<<<<<< HEAD
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
=======
    return render(request,'index.html')

def three_D(request):
    return render(request,'3D.html')

def about(request):
    return render(request,'about.html')

def AI_blog(request):
    return render(request,'AI(blog).html')

def chatbot(request):
    return render(request,'chatbot.html')

def cluster(request):
    return render(request,'cluster.html')

def contact(request):
    return render(request,'contact.html')

def E_commerce_development(request):
    return render(request,'E-commerce_development.html')

def Embedded(request):
    return render(request,'Embedded.html')

def healthcare(request):
    return render(request,'healthcare.html')

def imagerecognition(request):
    return render(request,'imagerecongnition.html')

def Intranet_solution(request):
    return render(request,'Intranet solution.html')

def machinelearning(request):
    return render(request,'machinelearning.html')

def mobile_application_development(request):
    return render(request,'mobile application development.html')

def NLP(request):
    return render(request,'NLP.html')

def PCB(request):
    return render(request,'PCB.html')

def Product(request):
    return render(request,'product.html')

def Python(request):
    return render(request,'Python.html')

def Robotic(request):
    return render(request,'Robotic.html')

def Robotics_blog(request):
    return render(request,'Robotics_blog.html')

def salesforce_system(request):
    return render(request,'salesforce system.html')

def SEO(request):
    return render(request,'SEO.html')

def Smart(request):
    return render(request,'Smart.html')

def Software_development(request):
    return render(request,'Software_development.html')

def STEM(request):
    return render(request,'STEM.html')

def training_pages(request):
    return render(request,'training pages.html')

def web_blog(request):
    return render(request,'web(blog).html')

>>>>>>> c38170ce87fc88192848e0d45e32a9477b23d0c9

