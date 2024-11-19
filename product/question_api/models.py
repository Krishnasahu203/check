from django.db import models
from django.core.exceptions import ValidationError



class Image(models.Model):
    image = models.ImageField(upload_to='uploads/', verbose_name="Image")
    name = models.CharField(max_length=100, unique=True, verbose_name="Image Name")

    def __str__(self):
        return self.name

# Create your models here.
class Question(models.Model):
    TEXT_ONLY = 'text'
    IMAGE_ONLY = 'image'

    ANSWER_TYPE_CHOICES = [
        (TEXT_ONLY, 'Text only'),
        (IMAGE_ONLY, 'Image only'),
    ]


    question_text = models.CharField(max_length=200, verbose_name="Question Text")
    is_mandatory = models.BooleanField(default=False, verbose_name="Mandatory")
    answer_type = models.CharField(
        max_length=5,
        choices=ANSWER_TYPE_CHOICES,
        default=TEXT_ONLY,
        verbose_name="Answer Type"
    )
    uploaded_image = models.ImageField(
        upload_to='uploads/',
        blank=True,
        null=True,
        verbose_name="Uploaded Image"
    ).BooleanField(default=True)

    selected_image = models.ForeignKey(
        Image,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Select Existing Image"
    )
    personalized_note = models.TextField(
        blank=True,
        null=True,
        verbose_name="Personalized Note"
    )

    def clean(self):
        # Validation: No images for text-only questions
        if self.answer_type == self.TEXT_ONLY and (self.uploaded_image or self.selected_image):
            raise ValidationError("For 'Text only' questions, images cannot be uploaded or selected.")
    
    def __str__(self):
        return self.question_text