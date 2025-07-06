from django.core.management.base import BaseCommand
from consulting.models import Service, ServiceBenefit, ServiceFAQ


class Command(BaseCommand):
    help = 'Seed the Service model with sample data.'
    
    def handle(self, *args, **options):
        data = [
            {
                'title': 'Consumer Product',
                'description': 'Expert advice on consumer product growth and strategy.',
                'detailed_description': 'Lorem ipsum is simply free text used by copytyping refreshing. Neque porro est qui dolorem ipsum quia quaed inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Aelltes port lacus quis enim var sed efficitur turpis gilla sed sit amet finibus eros. Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the ndustry standard dummy text ever since the 1500s.',
                'additional_description': 'It has survived not only five centuries. Lorem Ipsum is simply dummy text of the new design printng and type setting Ipsum take a look at our round. When an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting.',
                'image_url': 'https://images.unsplash.com/photo-1506744038136-46273834b3fb',
                'secondary_image_url': 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40',
                'icon': 'icon-creative',
                'highlight_text_1': 'Refresing to get such a touch. Duis aute irure dolor in oluptate.',
                'highlight_text_2': 'Velit esse cillum eu fugiat pariatur. Duis aute irure dolor in in voluptate.',
                'additional_content': 'When an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting. Lorem Ipsum has been the ndustry standard dummy text ever since the 1500s.',
                'benefits_title': 'Service Benefits',
                'benefits_description': 'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum.',
                'benefits': [
                    'In id diam nec nisi congue tincidunt',
                    'Pn malesuada purus a ligula dapibus',
                    'Vestibulum tincidunt arcu vel nisl',
                    'Sed tristique lorem non tesque'
                ],
                'faqs': [
                    {
                        'question': 'Interdum et malesuada fames ac ante ipsum',
                        'answer': 'Suspendisse finibus urna mauris, vitae consequat quam vel. Vestibulum leo ligula, vit commodo nisl Sed luctus venenatis pellentesque.'
                    },
                    {
                        'question': 'Maecenas condimentum sollicitudin ligula.',
                        'answer': 'Suspendisse finibus urna mauris, vitae consequat quam vel. Vestibulum leo ligula, vit commodo nisl Sed luctus venenatis pellentesque.'
                    },
                    {
                        'question': 'Duis rhoncus orci ut metus rhoncus.',
                        'answer': 'Suspendisse finibus urna mauris, vitae consequat quam vel. Vestibulum leo ligula, vit commodo nisl Sed luctus venenatis pellentesque.'
                    }
                ]
            },
            {
                'title': 'Banking Advising',
                'description': 'Specialist in banking and financial consulting.',
                'detailed_description': 'Comprehensive banking advisory services that help financial institutions navigate complex regulatory environments and optimize their operational efficiency. Our expertise spans across retail banking, corporate banking, and investment banking sectors.',
                'additional_description': 'We provide strategic guidance on digital transformation, risk management, and compliance frameworks. Our team of banking specialists brings decades of experience in helping banks modernize their operations while maintaining regulatory compliance.',
                'image_url': 'https://images.unsplash.com/photo-1464983953574-0892a716854b',
                'secondary_image_url': 'https://images.unsplash.com/photo-1560472354-b33ff0c44a43',
                'icon': 'icon-business',
                'highlight_text_1': 'Strategic banking solutions for modern financial institutions.',
                'highlight_text_2': 'Regulatory compliance and risk management expertise.',
                'additional_content': 'Our banking advisory services are designed to help financial institutions stay competitive in an rapidly evolving market while ensuring full compliance with regulatory requirements.',
                'benefits_title': 'Banking Benefits',
                'benefits_description': 'Comprehensive banking solutions tailored to your institution\'s needs.',
                'benefits': [
                    'Regulatory compliance expertise',
                    'Digital transformation guidance',
                    'Risk management strategies',
                    'Operational efficiency optimization'
                ],
                'faqs': [
                    {
                        'question': 'How do you help with regulatory compliance?',
                        'answer': 'We provide comprehensive compliance frameworks and ongoing support to ensure your institution meets all regulatory requirements.'
                    },
                    {
                        'question': 'What digital transformation services do you offer?',
                        'answer': 'Our services include digital strategy development, technology implementation, and change management for banking institutions.'
                    },
                    {
                        'question': 'How do you approach risk management?',
                        'answer': 'We develop customized risk management frameworks that align with your institution\'s specific needs and regulatory requirements.'
                    }
                ]
            },
            {
                'title': 'Marketing Rules',
                'description': 'Marketing and communications expertise for your business.',
                'detailed_description': 'Modern marketing strategies that drive engagement and conversion in today\'s digital landscape. We help businesses develop comprehensive marketing frameworks that align with their brand objectives and target audience needs.',
                'additional_description': 'Our marketing expertise covers digital marketing, content strategy, brand positioning, and campaign optimization. We work with businesses of all sizes to create marketing strategies that deliver measurable results.',
                'image_url': 'https://images.unsplash.com/photo-1515378791036-0648a3ef77b2',
                'secondary_image_url': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f',
                'icon': 'icon-global',
                'highlight_text_1': 'Data-driven marketing strategies that deliver results.',
                'highlight_text_2': 'Brand positioning and audience engagement expertise.',
                'additional_content': 'We believe in marketing strategies that are both creative and measurable, helping businesses connect with their audience while achieving their growth objectives.',
                'benefits_title': 'Marketing Benefits',
                'benefits_description': 'Comprehensive marketing solutions for business growth.',
                'benefits': [
                    'Digital marketing expertise',
                    'Brand strategy development',
                    'Campaign optimization',
                    'Analytics and reporting'
                ],
                'faqs': [
                    {
                        'question': 'What digital marketing services do you provide?',
                        'answer': 'We offer comprehensive digital marketing services including SEO, social media marketing, content marketing, and paid advertising campaigns.'
                    },
                    {
                        'question': 'How do you measure marketing success?',
                        'answer': 'We use advanced analytics and KPIs to track campaign performance, engagement rates, conversion metrics, and ROI.'
                    },
                    {
                        'question': 'Can you help with brand strategy?',
                        'answer': 'Yes, we develop comprehensive brand strategies including positioning, messaging, visual identity, and brand guidelines.'
                    }
                ]
            },
            {
                'title': 'Business Growth',
                'description': 'Strategies for sustainable business growth.',
                'detailed_description': 'Sustainable business growth strategies that help companies scale efficiently while maintaining operational excellence. Our approach focuses on identifying growth opportunities and developing actionable plans for implementation.',
                'additional_description': 'We work with businesses to optimize their operations, expand their market reach, and develop new revenue streams. Our growth strategies are designed to be sustainable and aligned with long-term business objectives.',
                'image_url': 'https://images.unsplash.com/photo-1465101046530-73398c7f28ca',
                'secondary_image_url': 'https://images.unsplash.com/photo-1553484771-371a605b060b',
                'icon': 'icon-mobile-analytics',
                'highlight_text_1': 'Sustainable growth strategies for long-term success.',
                'highlight_text_2': 'Market expansion and revenue optimization.',
                'additional_content': 'Our business growth consulting focuses on creating scalable systems and processes that support sustainable expansion while maintaining quality and efficiency.',
                'benefits_title': 'Growth Benefits',
                'benefits_description': 'Strategic growth solutions for scaling businesses.',
                'benefits': [
                    'Market expansion strategies',
                    'Revenue optimization',
                    'Operational efficiency',
                    'Strategic partnerships'
                ],
                'faqs': [
                    {
                        'question': 'How do you identify growth opportunities?',
                        'answer': 'We conduct comprehensive market analysis, competitive research, and internal assessments to identify the most promising growth opportunities.'
                    },
                    {
                        'question': 'What makes growth sustainable?',
                        'answer': 'Sustainable growth requires strong operational foundations, scalable systems, and strategies that can adapt to changing market conditions.'
                    },
                    {
                        'question': 'How do you measure growth success?',
                        'answer': 'We track key growth metrics including revenue growth, market share, customer acquisition, and operational efficiency indicators.'
                    }
                ]
            },
            {
                'title': 'Audit Marketing',
                'description': 'Comprehensive audit and marketing services.',
                'detailed_description': 'Comprehensive marketing audits that provide detailed insights into your current marketing performance and identify opportunities for improvement. Our audit process covers all aspects of your marketing strategy and execution.',
                'additional_description': 'We analyze your marketing channels, campaigns, messaging, and performance metrics to provide actionable recommendations for optimization. Our audits help businesses understand what\'s working and what needs improvement.',
                'image_url': 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40',
                'secondary_image_url': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71',
                'icon': 'icon-analysis',
                'highlight_text_1': 'Comprehensive marketing performance analysis.',
                'highlight_text_2': 'Data-driven insights and optimization recommendations.',
                'additional_content': 'Our marketing audits provide a complete picture of your marketing performance, helping you make informed decisions about where to invest your marketing budget for maximum impact.',
                'benefits_title': 'Audit Benefits',
                'benefits_description': 'Detailed marketing analysis for optimization.',
                'benefits': [
                    'Performance analysis',
                    'Channel optimization',
                    'ROI assessment',
                    'Strategic recommendations'
                ],
                'faqs': [
                    {
                        'question': 'What does a marketing audit include?',
                        'answer': 'Our audits cover all marketing channels, campaigns, messaging, analytics, and performance metrics to provide a comprehensive assessment.'
                    },
                    {
                        'question': 'How long does an audit take?',
                        'answer': 'Typical marketing audits take 2-4 weeks depending on the complexity of your marketing activities and the depth of analysis required.'
                    },
                    {
                        'question': 'What deliverables do you provide?',
                        'answer': 'We provide detailed audit reports with findings, recommendations, and action plans for improving your marketing performance.'
                    }
                ]
            },
            {
                'title': 'Financial Advice',
                'description': 'Financial planning and advice for individuals and businesses.',
                'detailed_description': 'Expert financial advisory services that help individuals and businesses make informed decisions about their financial future. Our comprehensive approach covers investment planning, risk management, and wealth preservation strategies.',
                'additional_description': 'We provide personalized financial advice based on your specific goals, risk tolerance, and financial situation. Our team of certified financial advisors brings expertise in investment management, tax planning, and retirement planning.',
                'image_url': 'https://images.unsplash.com/photo-1465101178521-c1a9136a3b99',
                'secondary_image_url': 'https://images.unsplash.com/photo-1554224155-8d04cb21cd6c',
                'icon': 'icon-creative-1',
                'highlight_text_1': 'Personalized financial strategies for your goals.',
                'highlight_text_2': 'Investment planning and wealth management expertise.',
                'additional_content': 'Our financial advisory services are designed to help you build, protect, and grow your wealth through strategic planning and informed decision-making.',
                'benefits_title': 'Financial Benefits',
                'benefits_description': 'Comprehensive financial planning and advisory services.',
                'benefits': [
                    'Investment portfolio management',
                    'Tax optimization strategies',
                    'Retirement planning',
                    'Risk management solutions'
                ],
                'faqs': [
                    {
                        'question': 'What financial services do you offer?',
                        'answer': 'We offer comprehensive financial planning, investment management, tax planning, retirement planning, and risk management services.'
                    },
                    {
                        'question': 'How do you develop financial strategies?',
                        'answer': 'We assess your financial situation, goals, and risk tolerance to develop personalized strategies that align with your objectives.'
                    },
                    {
                        'question': 'What qualifications do your advisors have?',
                        'answer': 'Our advisors are certified financial planners with extensive experience in investment management, tax planning, and financial advisory services.'
                    }
                ]
            },
        ]
        
        created = 0
        for entry in data:
            # Extract benefits and FAQs from entry
            benefits = entry.pop('benefits', [])
            faqs = entry.pop('faqs', [])
            
            # Create or get the service
            obj, was_created = Service.objects.get_or_create(
                title=entry['title'],
                defaults={
                    'description': entry['description'],
                    'detailed_description': entry['detailed_description'],
                    'additional_description': entry['additional_description'],
                    'image_url': entry['image_url'],
                    'secondary_image_url': entry['secondary_image_url'],
                    'icon': entry['icon'],
                    'highlight_text_1': entry['highlight_text_1'],
                    'highlight_text_2': entry['highlight_text_2'],
                    'additional_content': entry['additional_content'],
                    'benefits_title': entry['benefits_title'],
                    'benefits_description': entry['benefits_description'],
                    'is_active': True,
                }
            )
            
            if was_created:
                # Add benefits
                for benefit_text in benefits:
                    ServiceBenefit.objects.create(service=obj, text=benefit_text)
                
                # Add FAQs
                for faq in faqs:
                    ServiceFAQ.objects.create(
                        service=obj, 
                        question=faq['question'], 
                        answer=faq['answer']
                    )
                
                created += 1
        
        self.stdout.write(self.style.SUCCESS(f'Seeded {created} services.'))