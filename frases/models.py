from django.db import models


class Work(models.Model):
    """
    Unified model for movies and books
    """
    class WorkType(models.TextChoices):
        MOVIE = 'MOVIE', 'Movie'
        BOOK = 'BOOK', 'Book'
    
    type = models.CharField(
        max_length=10,
        choices=WorkType.choices,
        help_text="Type of work: MOVIE or BOOK"
    )
    title = models.CharField(max_length=200)  # ← FALTABA
    director = models.CharField(max_length=100, blank=True)  # ← blank=True para libros
    year = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'work'
        ordering = ['-created_at']
        verbose_name = 'Work'
        verbose_name_plural = 'Works'
    
    def __str__(self):
        return f"{self.title} ({self.get_type_display()})"


class Quote(models.Model):
    """
    Quote from a Movie or Book
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
        db_table = 'quote'
        ordering = ['-created_at']
        verbose_name = 'Quote'
        verbose_name_plural = 'Quotes'
    
    def __str__(self):
        return f"{self.work.title}: {self.text[:50]}..."