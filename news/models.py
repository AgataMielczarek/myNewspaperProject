from django.db import models
from django.contrib.auth.models import User

#title, email, owner(user, ktory utworzyl), date (utworzenia - dodawana automatycznie)
class Article(models.Model):
    title = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return self.title + ' ' + str(self.date)

    








