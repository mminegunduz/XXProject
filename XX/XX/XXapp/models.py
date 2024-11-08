from django.db import models

class Tweet(models.Model):
    kullaniciad= models.CharField(max_length=12)
    mesaj=models.CharField(max_length=350)

    def __str__(self):
        return f"Tweet kullanici: {self.kullaniciad} mesaj:{self.mesaj}"
