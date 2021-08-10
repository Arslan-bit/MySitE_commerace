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

    # Show name in Admin Panels

    def __str__(self):
        return self.produts_name


class contact_user(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default='')
    phone = models.CharField(max_length=50, default='')
    decs = models.CharField(max_length=1000, default='')

# Show name in Admin Panels
    def __str__(self):
        return self.email
