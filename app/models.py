from upload_to import UploadTo
from django.db import models


def my_upload_generator(instance, filename):
    filename = UploadTo.uuid_filename(filename)
    path = UploadTo.options_from_instance(instance)
    return UploadTo.upload_to(path, filename)


class AttachModel(models.Model):
    attachment = models.FileField(upload_to=UploadTo("media/attachments"))
