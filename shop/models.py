from django.db import models


# Create your models here.

class produts(models.Model):
    produts_id = models.AutoField
    produts_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default='')
    subcategory = models.CharField(max_length=50, default='')
    price = models.IntegerField(default=0)
    Decs = models.CharField(max_length=500)
    publish_list = models.DateField()
    img = models.ImageField(upload_to="shop/images", default='')

    def __str__(self):
        return self.produts_name
