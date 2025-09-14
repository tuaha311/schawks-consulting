from django.contrib import admin
from .models import (
    TeamMember,
    Service,
    ServiceBenefit,
    ServiceFAQ,
    Case,
    CaseKeypoint,
    Testimonial,
    BlogCategory,
    BlogPost,
    BlogComment,
    BookACall,
    BookACallGuest,
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


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publish_date", "is_published")
    search_fields = ("title", "author", "content")
    list_filter = ("is_published", "publish_date", "author")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("created_at", "updated_at")
    date_hierarchy = "publish_date"


@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ("name", "blog_post", "is_approved", "created_at")
    search_fields = ("name", "email", "comment")
    list_filter = ("is_approved", "created_at", "blog_post")
    readonly_fields = ("created_at", "updated_at")
    actions = ['approve_comments', 'unapprove_comments']

    def approve_comments(self, request, queryset):
        queryset.update(is_approved=True)
    approve_comments.short_description = "Approve selected comments"

    def unapprove_comments(self, request, queryset):
        queryset.update(is_approved=False)
    unapprove_comments.short_description = "Unapprove selected comments"


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "created_at")
    search_fields = ("name", "description")
    list_filter = ("is_active",)
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ("created_at", "updated_at")


class BookACallGuestInline(admin.TabularInline):
    model = BookACallGuest
    extra = 1
    fields = ('email', 'name')
    verbose_name = "Guest Email"
    verbose_name_plural = "Guest Emails"


@admin.register(BookACall)
class BookACallAdmin(admin.ModelAdmin):
    list_display = (
        "name", 
        "email", 
        "services_looking_for", 
        "business_stage", 
        "guest_count",
        "is_processed", 
        "created_at"
    )
    search_fields = ("name", "email", "website", "phone")
    list_filter = (
        "services_looking_for", 
        "business_stage", 
        "is_processed", 
        "created_at"
    )
    readonly_fields = ("created_at", "updated_at", "guest_count")
    list_editable = ("is_processed",)
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'phone', 'website')
        }),
        ('Business Details', {
            'fields': ('services_looking_for', 'business_stage', 'capital_amount')
        }),
        ('Processing', {
            'fields': ('is_processed', 'notes')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at', 'guest_count'),
            'classes': ('collapse',)
        }),
    )
    
    inlines = [BookACallGuestInline]
    
    actions = ['mark_as_processed', 'mark_as_unprocessed']
    
    def mark_as_processed(self, request, queryset):
        updated = queryset.update(is_processed=True)
        self.message_user(
            request,
            f'{updated} Book a Call request(s) marked as processed.'
        )
    mark_as_processed.short_description = "Mark selected requests as processed"
    
    def mark_as_unprocessed(self, request, queryset):
        updated = queryset.update(is_processed=False)
        self.message_user(
            request,
            f'{updated} Book a Call request(s) marked as unprocessed.'
        )
    mark_as_unprocessed.short_description = "Mark selected requests as unprocessed"


@admin.register(BookACallGuest)
class BookACallGuestAdmin(admin.ModelAdmin):
    list_display = ("email", "name", "book_a_call", "created_at")
    search_fields = ("email", "name", "book_a_call__name", "book_a_call__email")
    list_filter = ("created_at", "book_a_call__services_looking_for")
    readonly_fields = ("created_at",)
    list_select_related = ("book_a_call",)