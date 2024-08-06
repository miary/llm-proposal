from upload_to import UploadTo
from django.db import models


class AttachModel(models.Model):
    attachment = models.FileField(upload_to=UploadTo("media/attachments"))
