from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as gtl
import PIL


# Create your models here.
class User(models.Model):
    class GenderIdentity(models.IntegerChoices):
        AGENDER = 1, gtl('Agender')
        ANDROGYNE = 2, gtl('Androgyne')
        ANDROYNOUS = 3, gtl('Androgynous')
        BIGENDER = 4, gtl('Bigender')
        CIS = 5, gtl('Cis')
        CISGENDER = 6, gtl('Cisgender')
        CIS_FEMALE = 7, gtl('Cis Female')
        CIS_MALE = 8, gtl('Cis Male')
        CIS_MAN = 9, gtl('Cis Man')
        CIS_WOMAN = 10, gtl('Cis Woman')
        CISGENDER_FEMALE = 11, gtl('Cisgender Female')
        CISGENDER_MALE = 12, gtl('Cisgender Male')
        CISGENDER_MAN = 13, gtl('Cisgender Man')
        CISGENDER_WOMAN = 14, gtl('Cisgender Woman')
        FEMALE = 15, gtl('Female')
        FEMALE_TO_MALE = 16, gtl('Female to Male')
        FTM = 17, gtl('FTM')
        GENDER_FLUID = 18, gtl('Gender Fluid')
        GENDER_FUCK = 19, gtl('Gender F*ck')
        GENDER_NONCONFORMING = 20, gtl('Gender Nonconforming')
        GENDER_QUESTIONING = 21, gtl('Gender Questioning')
        GENDER_VARIANT = 22, gtl('Gender Variant')
        GENDERQUEER = 23, gtl('Genderqueer')
        MALE = 24, gtl('Male')
        MALE_TO_FEMALE = 25, gtl('Male to Female')
        MTF = 26, gtl('MTF')
        NEITHER = 27, gtl('Neither')
        NEUTROIS = 28, gtl('Neutrois')
        NON_BINARY = 29, gtl('Non-binary')
        OTHER = 30, gtl('Other')
        PANGENDER = 31, gtl('Pangender')
        TRANS = 32, gtl('Trans')
        TRANS_MAN = 33, gtl('Trans Man')
        TRANS_PERSON = 34, gtl('Trans Person')
        TRANS_WOMAN = 35, gtl('Trans Woman')
        TRANSFEMININE = 36, gtl('Transfeminine')
        TRANSGENDER = 37, gtl('Transgender')
        TRANSGENDER_FEMALE = 38, gtl('Transgender Female')
        TRANSGENDER_MALE = 39, gtl('Transgender Male')
        TRANSGENDER_MAN = 40, gtl('Transgender Man')
        TRANSGENDER_PERSON = 41, gtl('Transgender Person')
        TRANSGENDER_WOMAN = 42, gtl('Transgender Woman')
        TRANSMASCULINE = 43, gtl('Transmasculine')
        TRANSSEXUAL = 44, gtl('Transsexual')
        TRANSSEXUAL_FEMALE = 45, gtl('Transsexual Female')
        TRANSSEXUAL_MALE = 46, gtl('Transsexual Male')
        TRANSSEXUAL_MAN = 47, gtl('Transsexual Man')
        TRANSSEXUAL_PERSON = 48, gtl('Transsexual Person')
        TRANSSEXUAL_WOMAN = 49, gtl('Transsexual Woman')
        TWO_SPIRIT = 50, gtl('Two Spirit')  # For there are precisely 50.

    class ShowMe(models.TextChoices):  # as tinder implements sexuality.
        WOMEN = 'W', gtl('Women')
        MEN = 'M', gtl('Men')
        EVERYONE = 'E', gtl('Everyone')

    name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    description = models.CharField(max_length=500)
    gender_identity = models.IntegerField(choices=GenderIdentity.choices)
    show_me = models.CharField(max_length=1, choices=ShowMe.choices)
    same_orientation_first = models.BooleanField()
    last_sign_in = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField('self', symmetrical=False, related_name='like_target', blank=True)
    dislikes = models.ManyToManyField('self', symmetrical=False, related_name='dislike_target', blank=True)

    def __str__(self):
        return self.name


class Photo(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def blaine_or_not(user):
       
        #Helper function to upload files containing blaine to a different folder than
        #files containing not-blaine.
        
        if str(user).endswith("Blaine"):
            return 'blaine/'
        else:
            return ''

    picture = models.ImageField(upload_to=blaine_or_not(user), default="default.jpg")
    alt = models.CharField(max_length=140, default="")

    def __str__(self):
        return self.alt
    # I might want to think about a single user uploading multiple pictures later,
    # How can a user select which image they would like to use as default.
