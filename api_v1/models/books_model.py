from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, blank=False, null=False, related_name='fk_authors_books_books_id')
    genres = models.ManyToManyField('Genre', through='BookGenre', through_fields=('book', 'genre'), related_name='fk_genres_books_genres_id')
    page_count = models.PositiveIntegerField(null=True, blank=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    published_date = models.DateField()
    language = models.CharField(max_length=50)
    cover_image = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'books'
        ordering = ['-published_date', 'title']

    def __str__(self):
        return self.title