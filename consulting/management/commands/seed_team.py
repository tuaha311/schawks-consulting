from django.core.management.base import BaseCommand
from consulting.models import TeamMember

class Command(BaseCommand):
    help = 'Seed the TeamMember model with sample data.'

    def handle(self, *args, **options):
        data = [
            {
                'name': 'Sarah Albert',
                'role': 'Consultant',
                'bio': 'Expert in business strategy and growth.',
                'image_url': 'https://randomuser.me/api/portraits/women/1.jpg',
            },
            {
                'name': 'David Cooper',
                'role': 'Consultant',
                'bio': 'Specialist in financial consulting.',
                'image_url': 'https://randomuser.me/api/portraits/men/2.jpg',
            },
            {
                'name': 'Jessica Brown',
                'role': 'Consultant',
                'bio': 'Marketing and communications expert.',
                'image_url': 'https://randomuser.me/api/portraits/women/3.jpg',
            },
            {
                'name': 'Kevin Martin',
                'role': 'CO Founder',
                'bio': 'Founder and senior advisor.',
                'image_url': 'https://randomuser.me/api/portraits/men/4.jpg',
            },
        ]
        created = 0
        for entry in data:
            obj, was_created = TeamMember.objects.get_or_create(
                name=entry['name'],
                defaults={
                    'role': entry['role'],
                    'bio': entry['bio'],
                    'image_url': entry['image_url'],
                    'is_active': True,
                }
            )
            if was_created:
                created += 1
        self.stdout.write(self.style.SUCCESS(f'Seeded {created} team members.')) 