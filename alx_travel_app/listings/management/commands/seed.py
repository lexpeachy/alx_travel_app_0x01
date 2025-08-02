from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from listings.models import Listing
import random
from faker import Faker

User = get_user_model()
fake = Faker()

class Command(BaseCommand):
    help = 'Seeds the database with sample listings'

    def handle(self, *args, **options):
        self.stdout.write('Seeding data...')
        self.create_users()
        self.create_listings()
        self.stdout.write(self.style.SUCCESS('Successfully seeded data!'))

    def create_users(self):
        # Create admin user if not exists
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123'
            )
        
        # Create some regular users
        for i in range(5):
            username = f'user{i+1}'
            if not User.objects.filter(username=username).exists():
                User.objects.create_user(
                    username=username,
                    email=f'{username}@example.com',
                    password=f'user{i+1}123'
                )

    def create_listings(self):
        property_types = ['AP', 'HO', 'VI', 'CO', 'LO']
        users = User.objects.all()
        
        if not Listing.objects.exists():
            for i in range(20):
                owner = random.choice(users)
                city = fake.city()
                Listing.objects.create(
                    title=fake.sentence(nb_words=4),
                    description=fake.paragraph(nb_sentences=5),
                    address=fake.street_address(),
                    city=city,
                    country=fake.country(),
                    price_per_night=random.randint(50, 500),
                    property_type=random.choice(property_types),
                    num_bedrooms=random.randint(1, 5),
                    num_bathrooms=random.randint(1, 3),
                    max_guests=random.randint(1, 10),
                    amenities=', '.join(fake.words(nb=5)),
                    owner=owner
                )