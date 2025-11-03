from django.db import models

# Create your models here.
class Work(models.Model):
    """
    Unified model for movies and books
    """
    class WorkType(models.TextChoices):
        MOVIE = 'MOVIE'
        BOOK = 'BOOK'

    type = models.CharField(
        max_length=10,
        choices=WorkType.choices,
        help_text="Type of work: MOVIE or BOOK"
    )
    type = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    review = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Work'
        verbose_name_plural = 'Works'
    
    def __str__(self):
        return f"{self.title} ({self.get_type_display()})"
    

class Quote(models.Model):
    """
    Quote from a Movie or Book (only one required)
    """
    text = models.TextField()
    work = models.ForeignKey(
        Work,
        on_delete=models.CASCADE,
        related_name='quotes'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Quote'
        verbose_name_plural = 'Quotes'
    
    def __str__(self):
        return f"{self.work.title}:{self.text[:50]} "

