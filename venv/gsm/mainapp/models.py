from django.db import models

# Create your models here.

class Product(models.Model):
    titlu = models.CharField(max_length = 100)
    imagine = models.ImageField(upload_to = 'media')
    pret = models.FloatField()
    CATEGORY_CHOICES = [
        ('IPHONE', 'IPHONE'),
        ('SAMSUNG', 'SAMSUNG'),
        ('HUAWEI', 'HUAWEI'),
        ('CĂȘTI', 'CĂȘTI'),
        ('BATERII', 'BATERII'),
        ('CABLURI', 'CABLURI'),
        ('ÎNCĂRCĂTOARE', 'ÎNCĂRCĂTOARE'),
        ('IPHONE', 'IPHONE'),
    ]
    category = models.CharField(
        max_length = 20,
        choices = CATEGORY_CHOICES
    )
    nou = models.BooleanField(default=False)
