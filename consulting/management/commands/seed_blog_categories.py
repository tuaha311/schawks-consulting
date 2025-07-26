from django.core.management.base import BaseCommand
from consulting.models import BlogCategory


class Command(BaseCommand):
    """Populate the BlogCategory table with sample data for development/demo."""

    help = "Seed the database with blog categories. Run once for initial data."

    CATEGORIES = [
        {
            "name": "Consulting",
            "description": "Strategic consulting insights and best practices for business growth and transformation."
        },
        {
            "name": "Marketing",
            "description": "Marketing strategies, digital marketing trends, and customer engagement techniques."
        },
        {
            "name": "Technology",
            "description": "Technology trends, digital transformation, and innovation in business processes."
        },
        {
            "name": "Business & Finance",
            "description": "Financial planning, business strategy, and economic insights for sustainable growth."
        },
        {
            "name": "Bank Cryptcy",
            "description": "Banking regulations, cryptocurrency trends, and financial technology developments."
        },
    ]

    def handle(self, *args, **options):
        created_count = 0
        for data in self.CATEGORIES:
            obj, created = BlogCategory.objects.get_or_create(
                name=data["name"],
                defaults={
                    "description": data["description"],
                    "is_active": True,
                },
            )
            if created:
                created_count += 1
                
        self.stdout.write(self.style.SUCCESS(f"Seeded {created_count} blog categor{'y' if created_count == 1 else 'ies'}."))
