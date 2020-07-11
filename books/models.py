from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
import uuid

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField(default=0)
    cover = models.ImageField()

    def __str__(self):
        return "Book: {0} Author: {1}".format(self.title, self.author)
    
    def get_absolute_url(self):
        # return reverse("book_detail", args=[str(self.id)])
        return reverse("book_detail", kwargs={'pk':str(self.pk)})
    


class Review(models.Model): 
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    review = models.CharField(max_length=225)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.review