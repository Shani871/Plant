from django.urls import path

from PlantWebsite import views

urlpatterns = [

    path('', views.home, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('checkout/', views.checkout, name='checkout'),
    path('blog/', views.blog, name='blog'),
path('index/', views.index, name='index'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('checkout/', views.checkout, name='checkout'),

]