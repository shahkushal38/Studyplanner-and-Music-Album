from django.db import models

# Create your models here.
class Stock(models.Model):
    ticker=models.CharField( max_length=100)
    open = models.FloatField()
    # high = models.FloatField()
    # low = models.FloatField()
    close= models.FloatField()
    volume=models.IntegerField()

    def __str__(self):
        return self.ticker
    