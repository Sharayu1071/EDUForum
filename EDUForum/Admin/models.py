from django.db import models


# Create your models here.

class UserData(models.Model):
    # name=models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    email = models.EmailField()
    # contact = models.CharField(max_length=15)
    password = models.CharField(max_length=30)
    # file = models.FileField(upload_to="files")  # for file input
    file = models.FileField(upload_to='media', null=True)
    title = models.CharField(max_length=50, null=True)

    def _str_(self):
        return self.title




# class UserData_0(models.Model):
#     email = models.EmailField()
#     password = models.CharField(max_length=30)

