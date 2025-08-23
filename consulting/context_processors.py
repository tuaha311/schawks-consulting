from .models import Service, BlogCategory

def site_info(request):
    """
    Add site-wide information to the template context.
    """
    return {
        'SITE_NAME': 'Schawks Consulting',
        'SITE_DESCRIPTION': 'Strategic business consulting services',
        'PHONE_NUMBER': '+1 (555) 123-4567',
        'EMAIL': 'info@axial.com',
        'ADDRESS': '123 Business Ave, Suite 100, New York, NY 10001',
    }

def navigation_data(request):
    """
    Add navigation data to the template context.
    """
    # Get top 5 active services for navigation dropdown
    top_services = Service.objects.filter(is_active=True).order_by('created_at')[:5]
    
    # Get active blog categories for navigation dropdown
    blog_categories = BlogCategory.objects.filter(is_active=True).order_by('name')
    
    return {
        'nav_services': top_services,
        'nav_blog_categories': blog_categories,
    }
