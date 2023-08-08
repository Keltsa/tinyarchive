
from django.db import models
from model_utils.managers import InheritanceManager
from django.forms import CharField, URLField
from stdimage import StdImageField
from archive.consts import *


class ArchiveDocument(models.Model):
    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.id
    objects = InheritanceManager()
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=False)
    creator = models.CharField(max_length=50, blank="True")
    photo_image = StdImageField(
        upload_to="photographs/",
        variations={"thumbnail": {"width": 300, "height": 300}},
        null=True,
        blank = True,
    )


class AssociatedImage(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    associated_doc = models.ForeignKey(
        ArchiveDocument, blank=False, null=False, on_delete=models.CASCADE)
    creator = models.CharField(max_length=200, blank=True)
    photo_image = StdImageField(
        upload_to="photographs/",
        variations={"thumbnail": {"width": 300, "height": 300}},
        null=False
    )

    def __str__(self):
        return(self.photo_image.url)

class AudioRecording(ArchiveDocument):
    language = models.CharField(max_length=200)
    speaker = models.CharField(max_length=200)
    recording_date = models.DateField(auto_now=True)
    audio_file = models.FileField(upload_to="sounds/", null=True)

class Photograph(ArchiveDocument):
    photo_type = models.CharField(
        max_length=20,
        choices=list(
            Choices.PHOTO_TYPE_CHOICES.items()
        ),  # defining the constant as a dictionary for easy lookup in views.
    )


class Artifact(ArchiveDocument):
    MAT_OTHER = 'other'
    MAT_PLASTIC = 'plastic'
    MAT_CERAMIC = 'ceramic'
    MAT_GLASS = 'glass'
    MAT_METAL = 'metal'
    MAT_PORCELAIN = 'porcelain'

    MATERIAL_CHOICES = [(MAT_OTHER, "Other"),
                        (MAT_PLASTIC, "Plastic"),
                        (MAT_CERAMIC, "Ceramic"),
                        (MAT_GLASS, "Glass"),
                        (MAT_METAL,"Metal"),
                        (MAT_PORCELAIN, "Porcelain")]
    material = models.CharField(
        max_length=50, choices=MATERIAL_CHOICES, default=MAT_GLASS)
    dimensions = models.CharField(max_length=200, blank="True")
    color = models.CharField(max_length=200, blank="True")
    
    FUNC_ENT = 'entertainment'
    FUNC_ECON = 'economics'
    FUNC_COM = 'communication'
    FUNC_OTHER = 'other'

    FUNCTION_CHOICES = [(FUNC_ENT, "Entertainment"),
                        (FUNC_ECON, "Economics"),
                        (FUNC_COM, "Communication"),
                        (FUNC_OTHER, "Other")]
    function = models.CharField(
        max_length=50, choices=FUNCTION_CHOICES, default=FUNC_ENT)
    production_company = models.CharField(max_length=500, blank="True")
    
    PRICE_LOW = "<$50"
    PRICE_LOWMID = "$50-$100"
    PRICE_MID = "$101-$150"
    PRICE_MIDHIGH = "$151-$200"
    PRICE_HIGH = ">$201"
    
    PRICE_CHOICES = [(PRICE_LOW, "<$50"),
                     (PRICE_LOWMID, "$50-$100"),
                     (PRICE_MID, "$101-$150"),
                     (PRICE_MIDHIGH, "$151-$200"),
                     (PRICE_HIGH, ">$201")]
    price = models.CharField(
        max_length=50, choices=PRICE_CHOICES, default=PRICE_LOW)
    purchase_location = models.CharField(max_length = 500, blank="True")

    YEAR_0 = "2000"
    YEAR_1 = "2001"
    YEAR_2 = "2002"
    YEAR_3 = "2003"
    YEAR_4 = "2004"
    YEAR_5 = "2005"
    YEAR_6 = "2006"
    YEAR_7 = "2007"
    YEAR_8 = "2008"
    YEAR_9 = "2009"
    YEAR_10 = "2010"
    YEAR_11 = "2011"
    YEAR_12 = "2012"
    YEAR_13 = "2013"
    YEAR_14 = "2014"
    YEAR_15 = "2015"
    YEAR_16 = "2016"
    YEAR_17 = "2017"
    YEAR_18 = "2018"
    YEAR_19 = "2019"
    YEAR_20 = "2020"
    YEAR_21 = "2021"
    YEAR_22 = "2022"
    YEAR_23 = "2023"
    
    YEAR_CHOICES = [(YEAR_0, "2000"), (YEAR_1, "2001"), (YEAR_2, "2002"), (YEAR_3, "2003"),
                    (YEAR_4, "2004"), (YEAR_5, "2005"), (YEAR_6, "2006"), (YEAR_7, "2007"),
                    (YEAR_8, "2008"), (YEAR_9, "2009"), (YEAR_10, "2010"), (YEAR_11, "2011"),
                    (YEAR_12, "2012"), (YEAR_13, "2013"), (YEAR_14, "2014"), (YEAR_15, "2015"),
                    (YEAR_16, "2016"), (YEAR_17, "2017"), (YEAR_18, "2018"), (YEAR_19, "2019"),
                    (YEAR_20, "2020"), (YEAR_21, "2021"), (YEAR_22, "2022"), (YEAR_23, "2023")]
    purchase_year = models.CharField(
        max_length=50, choices=YEAR_CHOICES, default=YEAR_0)
    sentimental_value = models.TextField(max_length=10000, blank="True")
    model3d = models.URLField(max_length=500, blank="True")


class Document(ArchiveDocument):
    # might want to do something to standardize this later so people can't
    # just enter variant spellings for language names--a preformated list of standard names
    # and codes?
    language = models.CharField(max_length=200)
    transcription = models.TextField(blank=True, null=False)
