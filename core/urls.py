from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('service/', views.service, name = 'service'),
    path('query/', views.query, name = 'query'),
    path('book_appointment/', views.book_appointment, name = 'book_appointment'),
    path('appointment/', views.appointment, name = 'appointment'),
    path('feature/', views.feature, name = 'feature'),
    path('team/', views.team, name = 'team'),
    path('testimonial/', views.testimonial, name = 'testimonial'),
    path('contact/', views.contact, name = 'contact'),
    path('newsletter/', views.newsletter, name = 'newsletter'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
