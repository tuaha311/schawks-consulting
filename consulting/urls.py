from django.urls import path
from . import views

app_name = 'consulting'

urlpatterns = [
    # Home page
    path('', views.home, name='home'),
    # Services
    path('services/', views.services, name='services'),
    path('services/<slug:slug>/', views.service_detail, name='service_details'),
    # About
    path('about/', views.about, name='about'),
    # Team
    path('team/', views.team, name='team'),
    # Testimonials
    path('testimonials/', views.testimonials, name='testimonials'),
    # Blog
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_details'),
    # Contact
    path('contact/', views.contact, name='contact'),
    # Cases/Projects
    path('cases/', views.cases, name='cases'),
    path('cases/<slug:slug>/', views.case_detail, name='case_detail'),
    # FAQ
    path('faq/', views.faq, name='faq'),
]
