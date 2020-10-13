from django.urls import path

from . import views

urlpatterns = [
<<<<<<< HEAD
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

  


=======
    path("",views.index,name='Index'),
    path("3D/",views.three_D,name='3D'),
    path("about/",views.about,name='About'),
    path("AI_blog/",views.AI_blog,name='AI-Blog'),
    path("chatbot/",views.chatbot,name='Chatbot'),
    path("cluster/",views.cluster,name='Cluster'),
    path("contact/",views.contact,name='Contact'),
    path("e-commerce-development/",views.E_commerce_development,name='E-Commerce-Development'),
    path("embedded/",views.Embedded,name='Embedded'),
    path("healthcare/",views.healthcare,name='Healthcare'),
    path("imagerecognition/",views.imagerecognition,name='Imagerecognition'),
    path("intranet_solution/",views.Intranet_solution,name='Intranet-Solution'),
    path("machinelearning/",views.machinelearning,name='MachineLearning'),
    path("mobile_application_development/",views.mobile_application_development,name='Mobile-Application-Development'),
    path("NLP/",views.NLP,name='NLP'),
    path("PCB/",views.PCB,name='PCB'),
    path("product/",views.Product,name='Product'),
    path("python/",views.Python,name='Python'),
    path("robotic/",views.Robotic,name='Robotic'),
    path("robotics_blog/",views.Robotics_blog,name='Robotics-Blog'),
    path("salesforce_system/",views.salesforce_system,name='Salesforce-System'),
    path("SEO/",views.SEO,name='SEO'),
    path("smart/",views.Smart,name='Smart'),
    path("software_development/",views.Software_development,name='Software-Development'),
    path("STEM/",views.STEM,name='STEM'),
    path("training_pages/",views.training_pages,name='Training-Pages'),
    path("web_blog/",views.web_blog,name='Web-Blog'),
>>>>>>> c38170ce87fc88192848e0d45e32a9477b23d0c9
]