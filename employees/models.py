from django.db import models

class employee(models.Model):
    first_name=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    email_adress=models.EmailField(max_length=254,unique=True)
    phone_number=models.CharField(max_length=12,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.first_name.upper()}"
