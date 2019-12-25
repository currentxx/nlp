from django.db import models
# Create your models here.
class Kurlar (models.Model):
    doviz_ismi = models.CharField(max_length=10)
    alis = models.FloatField() #alis fiyati
    satis = models.FloatField() #satis fiyati
    fark = models.FloatField() #fark
    kur_kodu = models.CharField(max_length=10) #USD/TL
    def __str__(self):
        return self.doviz_ismi

class Ozet (models.Model):
    kelime = models.CharField(max_length=30)
    frequency = models.FloatField() #alis fiyati
    def __str__(self):
        return self.kelime

class OzetveTamMetin (models.Model):
    TamMetin = models.CharField(max_length=5000)
    OzetMetin = models.CharField(max_length=1000)
    def __str__(self):
        return self.OzetMetin