from django.core.management.base import BaseCommand
from consulting.models import Case, CaseKeypoint
from django.utils.text import slugify
from datetime import date


SAMPLE_CASES = [
    {
        "title": "Business Growth Through Expert Leadership",
        "client": "Jessica Brown",
        "category": "Consulting",
        "case_date": date(2024, 3, 15),
        "short_summary": (
            "Implemented leadership coaching and strategic planning that resulted "
            "in 40% year-over-year revenue growth."
        ),
        "description": (
            "Our consultants partnered with the executive team to craft a three-year "
            "growth roadmap, establish KPIs, and introduce a leadership academy. "
            "The initiative reinforced a culture of accountability and innovation, "
            "ultimately boosting EBITDA margins by 7 percentage points."
        ),
        "image_url": "https://images.unsplash.com/photo-1542744173-8e7e53415bb0",
        "keypoints": [
            "Established leadership academy",
            "40% YoY revenue growth",
            "EBITDA margin +7pp"
        ],
    },
    {
        "title": "Digital Campaigns for Business Success",
        "client": "BrightWave Inc.",
        "category": "Marketing",
        "case_date": date(2023, 11, 2),
        "short_summary": (
            "Delivered a multi-channel digital campaign that increased qualified leads "
            "by 230% within six months."
        ),
        "description": (
            "We designed and executed data-driven campaigns across search, social, and "
            "email channels. Marketing automation streamlined nurturing workflows, "
            "while A/B testing refined messaging for maximum conversion."
        ),
        "image_url": "https://images.unsplash.com/photo-1515378791036-0648a3ef77b2",
        "keypoints": [
            "Qualified leads +230%",
            "Automated nurturing workflows",
            "Optimised messaging via A/B testing"
        ],
    },
    {
        "title": "Finance Consulting and Business Strategy",
        "client": "Acme Bank",
        "category": "Finance",
        "case_date": date(2022, 9, 30),
        "short_summary": (
            "Optimised cost-to-income ratio by 12% through operational efficiency and "
            "digital process transformation."
        ),
        "description": (
            "Our team analysed branch-level performance and introduced a cloud-based "
            "workflow platform that cut processing times in half and improved customer "
            "satisfaction scores."
        ),
        "image_url": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40",
        "keypoints": [
            "Cost-to-income ratio -12%",
            "Processing time halved",
            "Customer satisfaction improved"
        ],
    },
    {
        "title": "Marketing Advice and Risk Management",
        "client": "Zenith Co.",
        "category": "Risk & Marketing",
        "case_date": date(2023, 2, 18),
        "short_summary": (
            "Balanced aggressive growth strategies with a robust risk framework, reducing "
            "campaign compliance incidents to zero."
        ),
        "description": (
            "We mapped regulatory requirements across regions and embedded compliance "
            "guardrails into marketing operations, safeguarding brand integrity during "
            "rapid expansion."
        ),
        "image_url": "https://images.unsplash.com/photo-1464983953574-0892a716854b",
        "keypoints": [
            "Zero compliance incidents",
            "Regulatory mapping across regions",
            "Embedded guardrails in operations"
        ],
    },
    {
        "title": "Substantial Business Market Rates",
        "client": "Omega Logistics",
        "category": "Supply Chain",
        "case_date": date(2024, 1, 10),
        "short_summary": (
            "Negotiated carrier agreements saving 18% annually while maintaining service "
            "levels across global routes."
        ),
        "description": (
            "Through a rigorous RFP process and data-driven network redesign, we optimised "
            "freight spend and improved OTIF (On-Time-In-Full) delivery by 6%."
        ),
        "image_url": "https://images.unsplash.com/photo-1553484771-371a605b060b",
        "keypoints": [
            "Freight spend -18%",
            "OTIF delivery +6%",
            "Carrier agreements negotiated"
        ],
    },
]


class Command(BaseCommand):
    help = "Seed the Case model with sample data."

    def handle(self, *args, **options):
        created = 0
        for data in SAMPLE_CASES:
            slug = slugify(data["title"])
            obj, was_created = Case.objects.get_or_create(slug=slug, defaults=data)
            if was_created:
                created += 1
            # create keypoints
            for text in data.get("keypoints", []):
                CaseKeypoint.objects.get_or_create(case=obj, text=text)
        self.stdout.write(self.style.SUCCESS(f"Seeded {created} Case records."))
