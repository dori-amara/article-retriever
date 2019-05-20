from django.core.management.base import BaseCommand
from retriever.utils import retrieve_and_save


class Command(BaseCommand):
    help = 'Retrieves and saves top 100 TechCrunch articles'

    def handle(self, *args, **options):
        self.stdout.write("Retrieving and saving top 100 TechCrunch articles...\n\n")
        retrieve_and_save('https://techcrunch.com/wp-json/wp/v2', 100)
        self.stdout.write("\n... complete.")
