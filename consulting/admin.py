from django.contrib import admin
from .models import (
    TeamMember,
    Service,
    ServiceBenefit,
    ServiceFAQ,
    Case,
    CaseKeypoint,
    Testimonial,
)


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "is_active", "created_at")
    search_fields = ("name", "role")
    list_filter = ("is_active",)




class ServiceBenefitInline(admin.TabularInline):
    model = ServiceBenefit
    extra = 1
    fields = ('text',)


class ServiceFAQInline(admin.TabularInline):
    model = ServiceFAQ
    extra = 1
    fields = ('question', 'answer')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "is_active", "created_at", "benefit_count", "faq_count")
    search_fields = ("title", "slug", "description")
    list_filter = ("is_active", "created_at")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'description', 'is_active')
        }),
        ('Content', {
            'fields': ('detailed_description', 'additional_description', 'additional_content')
        }),
        ('Images', {
            'fields': ('image', 'image_url', 'secondary_image', 'secondary_image_url'),
            'classes': ('collapse',)
        }),
        ('Styling', {
            'fields': ('icon', 'highlight_text_1', 'highlight_text_2'),
            'classes': ('collapse',)
        }),
        ('Benefits Section', {
            'fields': ('benefits_title', 'benefits_description'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    inlines = [ServiceBenefitInline, ServiceFAQInline]
    
    def benefit_count(self, obj):
        return obj.benefits.count()
    benefit_count.short_description = 'Benefits'
    
    def faq_count(self, obj):
        return obj.faqs.count()
    faq_count.short_description = 'FAQs'


@admin.register(ServiceBenefit)
class ServiceBenefitAdmin(admin.ModelAdmin):
    list_display = ('text', 'service', 'id')
    search_fields = ('text', 'service__title')
    list_filter = ('service',)
    list_select_related = ('service',)


@admin.register(ServiceFAQ)
class ServiceFAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'service', 'id')
    search_fields = ('question', 'answer', 'service__title')
    list_filter = ('service',)
    list_select_related = ('service',)
    fields = ('service', 'question', 'answer')


class CaseKeypointInline(admin.TabularInline):
    model = CaseKeypoint
    extra = 1
    fields = ("text",)


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    """Admin configuration for Case model."""
    list_display = ("title", "slug", "client", "category", "is_published", "created_at")
    search_fields = ("title", "client", "category")
    list_filter = ("is_published", "category", "case_date")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("created_at", "updated_at")
    inlines = (CaseKeypointInline,)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "is_active", "created_at")
    search_fields = ("name", "role", "text")
    list_filter = ("is_active",)
    readonly_fields = ("created_at", "updated_at")