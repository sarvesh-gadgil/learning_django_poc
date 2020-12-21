from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50, blank=False)
    email = models.CharField(max_length=50, blank=False, unique=True)
    password = models.CharField(max_length=50, blank=False)
    is_new = models.BooleanField(default=False)
    contact_no = models.IntegerField(default=0)
    is_married = models.BooleanField(default=False)

    class Meta:
        db_table = 'user_data'
