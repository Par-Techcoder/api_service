from django.db import models

class BookGenre(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, related_name='book_genres')
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, related_name='book_genres')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'books_genre'
        unique_together = ('book', 'genre')  # Ensure a book can only have one entry per genre

    def __str__(self):
        return f"{self.book.title} - {self.genre.name}"