from django.core.management.base import BaseCommand
from Backend.models import Profile,Project,Experience, Education,ContactMessage

class Command(BaseCommand):
    help = "Seed initial portfolio data"

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding portfolio data...")

        # PROFILE Section
        Profile.objects.all().delete()
        profile = Profile.objects.create(
            full_name="Linda Mutheu",
            bio="Backend Developer transitioning from Accounting, focused on Django, REST APIs, and scalable systems.",
            email="lindamutheu5@gmail.com",
            title="Backend Developer",
            location="Nairobi, Kenya",
            github_url="https://github.com/lindamutheu",
            linkedin_url="https://www.linkedin.com/in/linda-musyoki-507436261/",
        )

        # PROJECTS
        Project.objects.all().delete()
        Project.objects.create(
            title="Personal Portfolio Backend API",
            description="A scalable REST API powering a personal developer portfolio.",
            problem_statement="Needed a backend-first portfolio to demonstrate real-world backend skills.",
            solution="Built a Django REST API with PostgreSQL, Celery background tasks, and clean architecture.",
            tech_stack="Django, DRF, PostgreSQL, Celery",
            github_url="https://github.com/lindamutheu/Personal_portfolio_Backend"
        ),
        Project.objects.create(
            title="Online polling system",
            description="A robust online polling system for creating and managing polls.",
            problem_statement="Required a backend to support real-time polling and voting.",
            solution="Developed a Django REST API with real-time updates and secure voting mechanisms.",
            tech_stack="Django, DRF, PostgreSQL, Celery",
            github_url="https://github.com/lindamutheu/kura_nexus"
        ),
        Project.objects.create(
         title="Airbnb Clone Backend",
         description="Backend API for an Airbnb clone application.",
         problem_statement="Needed a backend to handle property listings, bookings, and user management.",
         solution="Created a Django REST API with JWT authentication, property management, and booking features.",
         tech_stack="Django, DRF, PostgreSQL, Celery, Redis, JWT",
         github_url="https://github.com/lindamutheu/alx_travel_app_0x03"
        ) 

        # EXPERIENCE
        Experience.objects.all().delete()

        Experience.objects.create(
            job_title="Backend Developer Intern",
            company_name="Optivus K Ltd",
            start_date="2025-11-21",
            responsibilities="Developed RESTful APIs using Django and DRF, implemented authentication, and optimized database queries."
        ),

        Experience.objects.create(
            job_title="Assistant Accountant",
            company_name="Jimkara Auto Spares Ltd",
            start_date="2023-03-06",
            responsibilities="Managed financial data, reconciliations, and reports."
        )

        # EDUCATION
        Education.objects.all().delete()
        Education.objects.create(
            institution_name="ALX Africa",
            degree="Certificate",
            field_of_study="Backend Engineering",
            start_year=2024,
            end_year=2025
        ),
        Education.objects.create(
            institution_name="South Eastern Kenya University",
            degree="Bachelor of Business Information Technology",
            field_of_study="Information Technology",
            start_year=2017,
            end_year=2021
        )


        # CONTACT MESSAGES
        ContactMessage.objects.all().delete()
        ContactMessage.objects.create(
            name="Linda Mutheu",
            email="lindamutheu5@gmail.com",
            subject="Inquiry about your portfolio",
            message="Hello, I'm interested in your work."
            sent_at="2026-01-01T10:00:00Z"
        )
        self.stdout.write(self.style.SUCCESS("Portfolio data seeded successfully"))
