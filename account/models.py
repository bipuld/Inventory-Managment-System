from django.db import models

from django.contrib.auth.models import User



from django.utils import timezone


class UserInfo(models.Model):
    GENDER_CHOOSE = (('male', 'Male'), ('female', 'Female'), ('other', 'Others'))
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="Inventory_User", primary_key=True)
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOOSE, default="male")
    phone = models.CharField(max_length=255)
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    country = models.CharField(max_length=25)
    company_name = models.CharField(max_length=55)
    designation = models.CharField(max_length=155)
    country = models.CharField(max_length=15)
    address = models.CharField(max_length=55)
    phone.help_text = "if has more than one no write separated with comma."
    image = models.ImageField(upload_to="profile", blank=True, null=True)
    is_verify = models.BooleanField(default=False)
    intro = models.TextField(blank=True, null=True)
    email = models.EmailField(unique=True)

    @property
    def full_name(self):
        if self.user:
            return f"{self.first_name} {self.last_name}"
        else:
            return None
    def __str__(self):
        if self.user:
            return f"{self.first_name} {self.last_name}"
        else:
            return "Anonymous User"


