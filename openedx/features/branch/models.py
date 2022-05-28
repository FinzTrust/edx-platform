"""
Model for Branch
"""


from typing_extensions import Required
from django.db import models
from django.core.validators import FileExtensionValidator


# Create your models here.

class Branch(models.Model):
    """
    Class for branch management
    """
    class Meta:
        app_label = 'branch'

    name_kh = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    short_name = models.CharField(max_length=12, unique=True)
    contact_person = models.CharField(max_length=255, null=True, blank=True)
    contact_number = models.CharField(max_length=15)
    contact_number_2 = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(max_length=1000, null=True, blank=True)
    logo = models.ImageField(
        blank=True,
        null=True,
        upload_to='branch/image',
        validators=[FileExtensionValidator(['jpg', 'png', 'ico', 'jpeg', 'giff'])]
        )
    website = models.CharField(max_length=60)
    email = models.CharField(max_length=60, null=True, blank=True)
    facebook = models.CharField(max_length=60, null=True, blank=True)
    telegram = models.CharField(max_length=15, null=True, blank=True)
    whatsapp = models.CharField(max_length=15, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name_en
