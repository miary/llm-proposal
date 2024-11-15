from django.db import models
from django.core.exceptions import ValidationError
import os

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.pdf', '.txt', '.docx', '.png']
    if ext.lower() not in valid_extensions:
        raise ValidationError('Unsupported file or document type.')

class ProposalModel(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=300, null=True)
    attachment = models.FileField(upload_to="attachments", null=True, validators=[validate_file_extension])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title # type: ignore
    
