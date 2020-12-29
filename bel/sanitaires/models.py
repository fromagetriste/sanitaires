from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator

# Create your models here.


class FichierFrais(models.Model):
    message_frais = models.FileField(
        upload_to='uploads/', max_length=100, validators=[FileExtensionValidator(allowed_extensions=['txt'])]
        ) # not safe
    # Don’t rely on validation of the file extension to determine a file’s type. Files can be renamed to have any extension no matter what data they contain.
    