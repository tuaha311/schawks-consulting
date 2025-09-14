from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.db import models
from .models import TeamMember, Service, Case, Testimonial, BlogPost, BlogComment, BlogCategory, BookACall, BookACallGuest

def home(request):
    """Home page view"""
    cases_qs = Case.objects.filter(is_published=True).order_by('-case_date', '-created_at')[:4]
    testimonials_qs = Testimonial.objects.filter(is_active=True)
    recent_posts = BlogPost.objects.filter(is_published=True).order_by('-publish_date')[:3]
    context = {
        'page_title': 'Home',
        'hero_title': 'Strategic Consulting for Business Growth',
        'hero_subtitle': 'Expert solutions for your business challenges',
        'cases': cases_qs,
        'testimonials': testimonials_qs,
        'recent_posts': recent_posts,
    }
    return render(request, 'index.html', context)

def about(request):
    """About page view"""
    team_members = TeamMember.objects.filter(is_active=True)
    testimonials_qs = Testimonial.objects.filter(is_active=True)
    context = {
        'page_title': 'About Us',
        'team_members': team_members,
        'testimonials': testimonials_qs,
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
    testimonials_qs = Testimonial.objects.filter(is_active=True)
    context = {
        'page_title': 'Testimonials',
        'testimonials': testimonials_qs,
    }
    return render(request, 'testimonials.html', context)

def blog(request):
    """Blog post list view with category filtering"""
    category_slug = request.GET.get('category')
    search_query = request.GET.get('search')
    
    posts = BlogPost.objects.filter(is_published=True)
    
    if category_slug:
        posts = posts.filter(category__slug=category_slug)
    
    if search_query:
        posts = posts.filter(
            models.Q(title__icontains=search_query) |
            models.Q(content__icontains=search_query) |
            models.Q(excerpt__icontains=search_query)
        )
    
    posts = posts.order_by('-publish_date')
    categories = BlogCategory.objects.filter(is_active=True)
    recent_posts = BlogPost.objects.filter(is_published=True).order_by('-publish_date')[:3]
    
    context = {
        'page_title': 'Our Blog',
        'posts': posts,
        'categories': categories,
        'recent_posts': recent_posts,
        'current_category': category_slug,
        'search_query': search_query,
    }
    return render(request, 'blog.html', context)

def blog_detail(request, slug):
    """Blog post detail view with comments and sidebar data"""
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    comments = post.comments.filter(is_approved=True).order_by('-created_at')
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment_text = request.POST.get('comment')
        
        if name and email and comment_text:
            BlogComment.objects.create(
                blog_post=post,
                name=name,
                email=email,
                comment=comment_text,
                is_approved=False  # Requires admin approval
            )
            messages.success(request, 'Your comment has been submitted and is awaiting approval.')
            return redirect('consulting:blog_details', slug=slug)
        else:
            messages.error(request, 'Please fill in all required fields.')
    
    # Sidebar data
    categories = BlogCategory.objects.filter(is_active=True)
    recent_posts = BlogPost.objects.filter(is_published=True).exclude(id=post.id).order_by('-publish_date')[:3]
    
    context = {
        'page_title': post.title,
        'post': post,
        'comments': comments,
        'comment_count': comments.count(),
        'categories': categories,
        'recent_posts': recent_posts,
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
    cases_qs = Case.objects.filter(is_published=True).order_by('-case_date', '-created_at')
    context = {
        'page_title': 'Our Cases',
        'cases': cases_qs,
    }
    return render(request, 'cases.html', context)

def case_detail(request, slug):
    """Case study detail view"""
    case_obj = get_object_or_404(Case, slug=slug, is_published=True)

    # Determine previous and next cases by chronological order (newest first)
    prev_case = (
        Case.objects.filter(is_published=True, case_date__lt=case_obj.case_date)
        .order_by('-case_date')
        .first()
        if case_obj.case_date else None
    )
    next_case = (
        Case.objects.filter(is_published=True, case_date__gt=case_obj.case_date)
        .order_by('case_date')
        .first()
        if case_obj.case_date else None
    )

    context = {
        'page_title': case_obj.title,
        'case': case_obj,
        'prev_case': prev_case,
        'next_case': next_case,
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

def coming_soon(request):
    """FAQ page view"""
    # faqs = FAQ.objects.filter(is_active=True)
    context = {
        'page_title': 'This Feature is Coming Soon',
        # 'faqs': faqs,
    }
    return render(request, 'coming-soon.html', context)

def error_404_view(request, exception):
    """Custom 404 error page"""
    return render(request, 'error.html', status=404)

def client_segment(request):
    """Client segments page view"""
    context = {
        'page_title': 'Client Segments',
    }
    return render(request, 'client-segment.html', context)


def book_a_call(request):
    """Book a Call page view with form handling"""
    if request.method == 'POST':
        try:
            # Create the main Book a Call record
            book_call = BookACall.objects.create(
                name=request.POST.get('name', '').strip(),
                website=request.POST.get('website', '').strip(),
                email=request.POST.get('email', '').strip(),
                phone=request.POST.get('phone', '').strip(),
                services_looking_for=request.POST.get('services_looking_for', ''),
                business_stage=request.POST.get('business_stage', ''),
                capital_amount=request.POST.get('capital_amount', '').strip(),
            )
            
            # Handle guest emails
            guest_emails = request.POST.getlist('guest_emails[]')
            guest_names = request.POST.getlist('guest_names[]')
            
            for i, email in enumerate(guest_emails):
                if email.strip():  # Only create if email is not empty
                    guest_name = guest_names[i] if i < len(guest_names) else ''
                    BookACallGuest.objects.create(
                        book_a_call=book_call,
                        email=email.strip(),
                        name=guest_name.strip()
                    )
            
            messages.success(request, 'Thank you! Your Book a Call request has been submitted successfully. We will get back to you soon.')
            return redirect('consulting:book_a_call')
            
        except Exception as e:
            messages.error(request, 'There was an error submitting your request. Please try again.')
    
    # Prepare choices for the template
    context = {
        'page_title': 'Book a Call',
        'service_choices': BookACall.SERVICE_CHOICES,
        'business_stage_choices': BookACall.BUSINESS_STAGE_CHOICES,
    }
    return render(request, 'book-a-call.html', context)
