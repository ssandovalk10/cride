

from django.db import models

from cride.utils.models import CRideModel

class Circle(CRideModel):

    name = models.CharField('circle name', max_length=140)
    slug_name = models.SlugField(unique=True, max_length=140)
    about = models.CharField('circle description', max_length=225)
    picture= models.ImageField(upload_to='circle/pictures', blank = True, null=True)

    #Stats
    rides_offered =models.PositiveIntegerField(default=0)
    rides_taken =models.PositiveIntegerField(default=0)

    verified = models.BooleanField(
        'verified circle',
        default=False,
        help_text='Verified Circles are also know as official communities.'
    )

    is_public = models.BooleanField(default=True,help_text='Public circles are listed in the main page.')

    is_limited = models.BooleanField(
        'limited',
        default=False,
        help_text='Limited circles can grow up to a fixed number of members.'
    )
    members_limit = models.PositiveIntegerField(default=0, help_text='If circle is limited, this will be the limit on the number of members.')

    def __str__(self):
        return self.name

    class Meta(CRideModel.Meta):

        ordering=['-rides_taken', '-rides_offered']