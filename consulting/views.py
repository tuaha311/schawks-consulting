from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from .models import TeamMember, Service

def home(request):
    """Home page view"""
    # Example context - update with your actual data
    context = {
        'page_title': 'Home',
        'hero_title': 'Strategic Consulting for Business Growth',
        'hero_subtitle': 'Expert solutions for your business challenges',
    }
    return render(request, 'index.html', context)

def about(request):
    """About page view"""
    context = {
        'page_title': 'About Us',
    }
    return render(request, 'about.html', context)

def services(request):
    """Services list view"""
    services = Service.objects.filter(is_active=True)
    context = {
        'page_title': 'Our Services',
        'services': services,
    }
    return render(request, 'services.html', context)

from django.shortcuts import render, get_object_or_404
from django.db import models
from .models import Service


def service_detail(request, slug):
    """Service detail view"""
    service = get_object_or_404(Service, slug=slug, is_active=True)
    
    # Prefetch related objects to avoid N+1 queries
    service = Service.objects.select_related().prefetch_related(
        'benefits', 'faqs'
    ).get(slug=slug, is_active=True)
    
    # Get benefits and FAQs
    benefits = service.get_benefits()
    faqs = service.get_faqs()
    
    context = {
        'page_title': service.title,
        'service': service,
        'benefits': benefits,
        'faqs': faqs,
    }
    return render(request, 'services-details.html', context)


def services_list(request):
    """Services list view"""
    services = Service.objects.filter(is_active=True).prefetch_related(
        'benefits', 'faqs'
    ).order_by('-created_at')
    
    context = {
        'page_title': 'Our Services',
        'services': services,
    }
    return render(request, 'services-list.html', context)

def team(request):
    """Team members list view"""
    team_members = TeamMember.objects.filter(is_active=True)
    context = {
        'page_title': 'Our Team',
        'team_members': team_members,
    }
    return render(request, 'team.html', context)

def testimonials(request):
    """Testimonials view"""
    # testimonials = Testimonial.objects.filter(is_active=True)
    context = {
        'page_title': 'Testimonials',
        # 'testimonials': testimonials,
    }
    return render(request, 'testimonials.html', context)

def blog(request):
    """Blog post list view"""
    # posts = BlogPost.objects.filter(is_published=True).order_by('-publish_date')
    context = {
        'page_title': 'Our Blog',
        # 'posts': posts,
    }
    return render(request, 'blog.html', context)

def blog_detail(request, slug):
    """Blog post detail view"""
    # post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    context = {
        'page_title': 'Blog Details',
        # 'post': post,
    }
    return render(request, 'blog-details.html', context)

def contact(request):
    """Contact form view"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Send email
        send_mail(
            f'Contact Form: {subject}',
            f'From: {name} <{email}>\n\n{message}',
            settings.DEFAULT_FROM_EMAIL,
            [settings.CONTACT_EMAIL],
            fail_silently=False,
        )
        
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('consulting:contact')
    
    context = {
        'page_title': 'Contact Us',
    }
    return render(request, 'contact.html', context)

def cases(request):
    """Case studies list view"""
    # cases = CaseStudy.objects.filter(is_published=True)
    context = {
        'page_title': 'Our Cases',
        # 'cases': cases,
    }
    return render(request, 'cases.html', context)

def case_detail(request, slug):
    """Case study detail view"""
    # case = get_object_or_404(CaseStudy, slug=slug, is_published=True)
    context = {
        'page_title': 'Case Study Details',
        # 'case': case,
    }
    return render(request, 'case-details.html', context)

def faq(request):
    """FAQ page view"""
    # faqs = FAQ.objects.filter(is_active=True)
    context = {
        'page_title': 'Frequently Asked Questions',
        # 'faqs': faqs,
    }
    return render(request, 'faq.html', context)

def error_404_view(request, exception):
    """Custom 404 error page"""
    return render(request, 'error.html', status=404)
