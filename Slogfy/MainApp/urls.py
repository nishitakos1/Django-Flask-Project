from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('about.html/', views.about, name='About'),
    path('contact.html/', views.contact, name='Contact Us'),
    path('product.html/', views.productview, name='Our product'),
    path('trainingpages.html/', views.training, name='Training Course'),
    path('Robotics(blogs).html/', views.rblog, name='rBlog'),
    path('AI(blog).html/', views.ablog, name='aBlog'),
    path('web(blog).html/', views.weblog, name='weBlog'),
    path('Embedded.html/', views.emblog, name='emBlog'),
    path('PCB.html/', views.pcblog, name='pcBlog'),
    path('3D.html/', views.dblog, name='dBlog'),
    path('STEM.html/', views.stblog, name='stBlog'),
    path('Smart.html/', views.smablog, name='smaBlog'),
    path('Robotic.html/', views.roblog, name='roBlog'),
    path('machinelearning.html/', views.mablog, name='maBlog'),
    path('chatbot.html/', views.chatblog, name='chatBlog'),
    path('cluster.html/', views.clasblog, name='clasBlog'),
    path('E-commerce_development.html/', views.ecomblog, name='ecomBlog'),
    path('healthcare.html/', views.healthblog, name='healthBlog'),
    path('imagerecongnition.html/', views.imgblog, name='imgBlog'),
    path('intranetsolution.html/', views.inblog, name='inBlog'),
    path('mobileapplicationdevelopment.html/', views.mobblog, name='mobBlog'),
    path('NLP.html/', views.nlblog, name='nlBlog'),
    path('Python.html/', views.pyblog, name='pyBlog'),
    path('salesforcesystem.html/', views.selblog, name='selBlog'),
    path('SEO.html/', views.seblog, name='seBlog'),
    path('Software_development.html/', views.sofblog, name='sofBlog'),
    path('web(blog).html/', views.webblog, name='webBlog'),

  


]