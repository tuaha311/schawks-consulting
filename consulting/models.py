from django.db import models
from django.utils.text import slugify

# Create your models here.

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='team/', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def display_image(self):
        if self.image:
            return self.image.url
        elif self.image_url:
            return self.image_url
        return ''

    def __str__(self):
        return f"{self.name} ({self.role})"

class Service(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    description = models.TextField(blank=True)
    
    # Main content fields
    detailed_description = models.TextField(blank=True, help_text='Detailed description paragraph 1')
    additional_description = models.TextField(blank=True, help_text='Additional description paragraph 2')
    
    # Images
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    secondary_image = models.ImageField(upload_to='services/', blank=True, null=True)
    secondary_image_url = models.URLField(blank=True, null=True)
    
    # Icon and styling
    icon = models.CharField(max_length=100, blank=True, help_text='CSS class for icon, e.g. icon-creative')
    
    # Text box content
    highlight_text_1 = models.TextField(blank=True, help_text='First highlight text box')
    highlight_text_2 = models.TextField(blank=True, help_text='Second highlight text box')
    
    # Additional content
    additional_content = models.TextField(blank=True, help_text='Additional paragraph content')
    
    # Service Benefits (moved to related model)
    benefits_title = models.CharField(max_length=200, default='Service Benefits')
    benefits_description = models.TextField(blank=True, help_text='Benefits description')
    
    # Status and timestamps
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def display_image(self):
        if self.image:
            return self.image.url
        elif self.image_url:
            return self.image_url
        return ''
    
    def display_secondary_image(self):
        if self.secondary_image:
            return self.secondary_image.url
        elif self.secondary_image_url:
            return self.secondary_image_url
        return ''
    
    def __str__(self):
        return self.title
    
    def get_benefits(self):
        return self.benefits.all()
    
    def get_faqs(self):
        return self.faqs.all()


class ServiceBenefit(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='benefits')
    text = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.text} (Service: {self.service.title})"


class ServiceFAQ(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='faqs')
    question = models.CharField(max_length=300)
    answer = models.TextField()
    
    def __str__(self):
        return f"FAQ for {self.service.title}: {self.question}"


class Case(models.Model):
    """A case study / project showcase."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)

    # Images
    image = models.ImageField(upload_to='cases/', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)

    # Meta info
    client = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=200, blank=True)
    case_date = models.DateField(blank=True, null=True)

    # Content
    short_summary = models.TextField(blank=True, help_text="Short blurb displayed on list page")
    description = models.TextField(blank=True, help_text="Full description shown on detail page")

    # Status & timestamps
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def display_image(self):
        if self.image:
            return self.image.url
        elif self.image_url:
            return self.image_url
        return ''

    def __str__(self):
        return self.title
    
class CaseKeypoint(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='keypoints')
    text = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.text} (Case: {self.case.title})"


class Testimonial(models.Model):
    """Client testimonials displayed on testimonials page."""
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True)
    text = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def display_image(self):
        if self.image:
            return self.image.url
        elif self.image_url:
            return self.image_url
        return ''

    def __str__(self):
        return self.name


class BlogCategory(models.Model):
    """Categories for blog posts."""
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, max_length=100)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Blog Categories"
        ordering = ['name']


class BlogPost(models.Model):
    """Blog posts for the consulting website."""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, null=True, blank=True)
    author = models.CharField(max_length=100, default='Admin')
    excerpt = models.TextField(blank=True, help_text="Short excerpt for list page")
    content = models.TextField(help_text="Full blog post content")
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    publish_date = models.DateTimeField()
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def display_image(self):
        if self.image:
            return self.image.url
        elif self.image_url:
            return self.image_url
        return ''

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publish_date']


class BlogComment(models.Model):
    """Comments on blog posts."""
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.blog_post.title}"

    class Meta:
        ordering = ['-created_at']