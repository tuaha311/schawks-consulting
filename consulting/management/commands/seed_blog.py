from django.core.management.base import BaseCommand
from consulting.models import BlogPost
from django.utils import timezone
from datetime import timedelta


class Command(BaseCommand):
    """Populate the BlogPost table with sample data for development/demo."""

    help = "Seed the database with sample blog posts. Run once for initial data."

    SAMPLE_POSTS = [
        {
            "title": "Strategic Leadership in Times of Digital Transformation",
            "author": "Sarah Chen",
            "excerpt": (
                "Digital transformation requires more than technology—it demands strategic leadership "
                "that can navigate uncertainty while inspiring teams to embrace change."
            ),
            "content": (
                "In today's rapidly evolving business landscape, digital transformation has become "
                "a critical imperative for organizations seeking to remain competitive. However, "
                "successful transformation extends far beyond implementing new technologies.\n\n"
                "Strategic leaders must cultivate a culture of innovation while maintaining operational "
                "excellence. This requires clear communication, stakeholder alignment, and the ability "
                "to make data-driven decisions under pressure.\n\n"
                "Our experience working with Fortune 500 companies has shown that the most successful "
                "transformations are those led by executives who understand both the technical and "
                "human elements of change management."
            ),
            "image_url": "https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&w=800&q=80",
            "days_ago": 5,
        },
        {
            "title": "Financial Restructuring: A Roadmap to Sustainable Growth",
            "author": "Michael Rodriguez",
            "excerpt": (
                "When cash flow challenges threaten business continuity, strategic financial "
                "restructuring can provide the foundation for long-term sustainability and growth."
            ),
            "content": (
                "Financial distress doesn't have to signal the end of a business journey. With the "
                "right restructuring strategy, companies can emerge stronger and more resilient.\n\n"
                "The key lies in early identification of warning signs, stakeholder engagement, "
                "and the development of realistic turnaround plans that address both immediate "
                "liquidity concerns and long-term strategic positioning.\n\n"
                "Our team has successfully guided over 200 companies through complex restructuring "
                "processes, achieving an average debt reduction of 40% while preserving jobs and "
                "maintaining customer relationships."
            ),
            "image_url": "https://images.unsplash.com/photo-1554224155-6726b3ff858f?auto=format&fit=crop&w=800&q=80",
            "days_ago": 12,
        },
        {
            "title": "Building High-Performance Teams in Remote Work Environments",
            "author": "Dr. Emily Watson",
            "excerpt": (
                "Remote work has fundamentally changed team dynamics. Learn how to build cohesive, "
                "high-performing teams that thrive in distributed work environments."
            ),
            "content": (
                "The shift to remote work has created new challenges for team leadership and "
                "collaboration. Traditional management approaches often fall short in virtual "
                "environments, requiring leaders to adapt their strategies.\n\n"
                "Successful remote teams share common characteristics: clear communication protocols, "
                "well-defined goals, regular check-ins, and a strong culture of trust and accountability.\n\n"
                "Through our research with over 150 remote teams, we've identified five critical "
                "success factors that distinguish high-performing distributed teams from their "
                "struggling counterparts."
            ),
            "image_url": "https://images.unsplash.com/photo-1600880292203-757bb62b4baf?auto=format&fit=crop&w=800&q=80",
            "days_ago": 18,
        },
        {
            "title": "Supply Chain Optimization in an Uncertain World",
            "author": "James Liu",
            "excerpt": (
                "Global supply chain disruptions have exposed vulnerabilities in traditional logistics "
                "models. Discover strategies for building resilient, adaptive supply networks."
            ),
            "content": (
                "Recent global events have highlighted the fragility of traditional supply chain "
                "models. Companies that relied heavily on single-source suppliers or just-in-time "
                "inventory found themselves particularly vulnerable.\n\n"
                "Building supply chain resilience requires a fundamental shift from cost optimization "
                "to risk mitigation. This includes diversifying supplier bases, implementing advanced "
                "analytics for demand forecasting, and creating flexible logistics networks.\n\n"
                "Our supply chain optimization projects have helped clients reduce costs by an average "
                "of 15% while improving delivery reliability by 25%."
            ),
            "image_url": "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=800&q=80",
            "days_ago": 25,
        },
        {
            "title": "Customer Experience Innovation: Beyond Digital Touchpoints",
            "author": "Lisa Park",
            "excerpt": (
                "True customer experience innovation goes beyond digital interfaces to create "
                "meaningful, memorable interactions that drive loyalty and advocacy."
            ),
            "content": (
                "In an era of digital saturation, companies are discovering that technology alone "
                "cannot create exceptional customer experiences. The most successful organizations "
                "focus on understanding customer emotions and motivations.\n\n"
                "Effective CX innovation requires a holistic approach that considers every touchpoint "
                "in the customer journey. This includes not just digital interfaces, but also "
                "human interactions, physical environments, and post-purchase support.\n\n"
                "Our CX transformation initiatives have generated an average NPS improvement of 35 "
                "points and increased customer lifetime value by 28%."
            ),
            "image_url": "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?auto=format&fit=crop&w=800&q=80",
            "days_ago": 30,
        },
        {
            "title": "Data-Driven Decision Making: From Analytics to Action",
            "author": "Robert Kim",
            "excerpt": (
                "Organizations are drowning in data but starving for insights. Learn how to transform "
                "raw data into actionable intelligence that drives business results."
            ),
            "content": (
                "The promise of big data has largely gone unfulfilled for many organizations. Despite "
                "massive investments in analytics platforms and data science teams, many companies "
                "struggle to translate insights into meaningful business outcomes.\n\n"
                "The challenge isn't technical—it's organizational. Successful data-driven companies "
                "have built cultures that value evidence-based decision making and have established "
                "clear processes for turning insights into action.\n\n"
                "Our data strategy engagements have helped clients increase decision-making speed by "
                "40% while improving outcome accuracy by 60%."
            ),
            "image_url": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80",
            "days_ago": 35,
        },
    ]

    def handle(self, *args, **options):
        created_count = 0
        now = timezone.now()
        
        for data in self.SAMPLE_POSTS:
            publish_date = now - timedelta(days=data["days_ago"])
            
            obj, created = BlogPost.objects.get_or_create(
                title=data["title"],
                defaults={
                    "author": data["author"],
                    "excerpt": data["excerpt"],
                    "content": data["content"],
                    "image_url": data["image_url"],
                    "publish_date": publish_date,
                    "is_published": True,
                },
            )
            if created:
                created_count += 1
                
        self.stdout.write(self.style.SUCCESS(f"Seeded {created_count} blog post(s)."))
