from django.utils import timezone
from django.core.management import BaseCommand
from cover.models import BadCover, CoverImage

############### management commands seeder
class Command(BaseCommand):

    # seeder command to create bad covers
    help = 'create bad covers'

    def handle(self, *args, **options):

        date_added = timezone.now()

        coverimage_1 = CoverImage.objects.create(
            url='https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1381743337l/16590010.jpg',
            cover_client='Good Reads',
            date_added=date_added,
            original='d7642/d7027/9780444594044.jpeg'
        )

        coverimage_2 = CoverImage.objects.create(
            url='https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1361649303l/2696725.jpg',
            cover_client='GoodReads',
            date_added=date_added,
            original='/library/porrima/data/cover/475a9/5514f/9780140480283.jpeg'
        )

        coverimage_3 = CoverImage.objects.create(
            url='http://covers.openlibrary.org/b/LCCN/64021206-L.jpg?default=false',
            cover_client='OpenLibrary',
            date_added=date_added,
            original='/library/porrima/data/cover/63592/d6978/64021206.jpeg'
        )

        BadCover.objects.get_or_create(
            number=9780444594044,
            number_type='ISBN',
            cover_image_id=coverimage_1.id,
            date_added=date_added,
            annotation=BadCover.Annotations.CROP_REQUIRED
        )

        BadCover.objects.get_or_create(
            number=9780140480283,
            number_type='ISBN',
            cover_image_id=coverimage_2.id,
            date_added=date_added,
            annotation=BadCover.Annotations.BLURRY_PHOTO
        )

        BadCover.objects.get_or_create(
            number=64021206,
            number_type='lccn',
            cover_image_id=coverimage_3.id,
            date_added=date_added,
            annotation=BadCover.Annotations.GENERIC_COVER
        )
