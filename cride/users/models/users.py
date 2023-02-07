from django.db import models
from django.db.models import CharField
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

#utilities
from cride.utils.models import CRideModel


class User(CRideModel, AbstractUser):
    """
    Default custom user model for cride.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exist.'
        }
    )
    phone_regex = RegexValidator(
        regex= r'\+?1?\d{9,15}$',
        message= "Phone number must be entered in the format: +9999999. Up to 15 digits allowed"
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS=['username', 'first_name', 'last_name']

    is_client = models.BooleanField(
        'client status',
        default=True,
        help_text=('Help easily distinguish users and perform')
    )
    is_verfied = models.BooleanField(
        'verified',
        default=False,
        help_text=('Is verified user')
    )
    name = CharField(("Name of User"), blank=True, max_length=255)
    #first_name = None  # type: ignore
    #last_name = None  # type: ignore

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username