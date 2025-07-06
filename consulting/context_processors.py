def site_info(request):
    """
    Add site-wide information to the template context.
    """
    return {
        'SITE_NAME': 'Axial Consulting',
        'SITE_DESCRIPTION': 'Strategic business consulting services',
        'PHONE_NUMBER': '+1 (555) 123-4567',
        'EMAIL': 'info@axial.com',
        'ADDRESS': '123 Business Ave, Suite 100, New York, NY 10001',
    }
