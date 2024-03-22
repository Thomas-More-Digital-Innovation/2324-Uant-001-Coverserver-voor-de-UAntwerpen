
##################### path in urls.py of cover app
# path(r'badcovers/', views.list_bad_covers, name='list_bad_covers'),


##################### views function to list badcovers in cover app

# def list_bad_covers(request):

#     annotation_request = request.GET.get('annotation')
#     badcovers = BadCover.objects.all()

#     if annotation_request:
#         badcovers = badcovers.filter(annotation=annotation_request)

#     context = {
#         'badcovers': badcovers,
#         'form': CoverAnnotationFilterForm(),
#     }
#     return render(request, 'cover/badcovers.html', context)


##################### in modelfactories.py of cover app
# faker = FakerClass()

# class BadCoverFactory(DjangoModelFactory):
#     class Meta:
#         model = BadCover

#     number = Sequence(lambda n: _generate_isbn_13(n))
#     number_type = get_number_type_name(ISBN)
#     cover_image = SubFactory(CoverImageFactory)
#     annotation = faker.random_element(elements=[x[0] for x in BadCover.Annotations.choices])


############## models.py of cover app
# from django.db import models

# class BadCover(Model):
#     class Annotations(models.TextChoices):
#         CROP_REQUIRED = 'cropping required', 'cropping required'
#         BLURRY_PHOTO = 'blurry photo', 'blurry photo'
#         WRONG_BOOK = 'wrong book', 'wrong book'
#         GENERIC_COVER = 'generic cover', 'generic cover'

#     number = CharField(max_length=32)
#     number_type = CharField(max_length=32)
#     cover_image = ForeignKey(CoverImage, on_delete=SET_NULL, blank=True, null=True)
#     date_added = DateTimeField(auto_now_add=True)
#     annotation = CharField(max_length=32, choices=Annotations.choices)

#     class Meta:
#         unique_together = ('number_type', 'number')
#         index_together = ('number_type', 'number')
#         indexes = [
#             Index(
#                 name='bad_cover',
#                 fields=['number_type', 'number']
#             )
#         ]

#     def __str__(self):
#         return f'{self.number} ({self.number_type})'

################ forms.py cover app
# class CoverAnnotationFilterForm(forms.Form):
#     annotation = forms.ChoiceField(choices=BadCover.Annotations.choices)

# from cover.models import BadCover
