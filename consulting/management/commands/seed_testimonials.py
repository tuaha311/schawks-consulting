from django.core.management.base import BaseCommand
from consulting.models import Testimonial


class Command(BaseCommand):
    """Populate the Testimonial table with sample data for development/demo."""

    help = "Seed the database with sample testimonials. Run once for initial data."

    SAMPLE_TESTIMONIALS = [
        {
            "name": "Christine Rose",
            "role": "CEO, Rose Industries",
            "text": (
                "Axial's strategic insights transformed our operations. Their hands-on approach and deep "
                "expertise accelerated our growth trajectory beyond expectations."
            ),
            "image_url": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=400&q=80",
        },
        {
            "name": "Mike Hardson",
            "role": "VP Marketing, Hardson Co.",
            "text": (
                "Working with Axial felt like an extension of our team. They delivered measurable results and "
                "empowered our staff with new capabilities."
            ),
            "image_url": "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?auto=format&fit=crop&w=400&q=80",
        },
        {
            "name": "Laura Smith",
            "role": "COO, Smith Logistics",
            "text": (
                "Their analytical rigour uncovered hidden efficiencies in our supply chain, saving us millions "
                "within the first quarter of implementation."
            ),
            "image_url": "https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e?auto=format&fit=crop&w=400&q=80",
        },
        {
            "name": "Samuel Green",
            "role": "Founder, GreenTech",
            "text": (
                "The team at Axial delivered a market entry strategy that positioned us for rapid adoption "
                "while staying true to our mission-driven culture."
            ),
            "image_url": "https://images.unsplash.com/photo-1492562080023-ab3db95bfbce?auto=format&fit=crop&w=400&q=80",
        },
        {
            "name": "Isabella Turner",
            "role": "Chief HR Officer, Turner Group",
            "text": (
                "Axial's leadership development program has been a game-changer for our managers, boosting "
                "engagement and performance across departments."
            ),
            "image_url": "https://images.unsplash.com/photo-1529626455594-4ff0802cfb7e?auto=format&fit=crop&w=400&q=80",
        },
        {
            "name": "Daniel Perez",
            "role": "Head of Finance, Perez Holdings",
            "text": (
                "Their financial restructuring expertise not only stabilised our cash flow but also paved the "
                "way for sustainable long-term growth."
            ),
            "image_url": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=400&q=80",
        },
    ]

    def handle(self, *args, **options):
        created_count = 0
        for data in self.SAMPLE_TESTIMONIALS:
            obj, created = Testimonial.objects.get_or_create(
                name=data["name"],
                defaults={
                    "role": data["role"],
                    "text": data["text"],
                    "image_url": data["image_url"],
                    "is_active": True,
                },
            )
            if created:
                created_count += 1
        self.stdout.write(self.style.SUCCESS(f"Seeded {created_count} testimonial(s)."))
