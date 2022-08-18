from django.db import models
import uuid
from datetime import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.


USER_TYPE_CHOICES = (
    ('admin', 'Admin'),
    ('customer', 'Customer'),
)


class User(AbstractUser):
    user_type = models.CharField(
        max_length=20, choices=USER_TYPE_CHOICES, default='customer')
    email = models.EmailField(null = True,blank = True)
    password = models.CharField(max_length=128, verbose_name='password' , default= "akashjoshi") #TODO: No longer being used
    uuid = models.CharField(max_length=30, blank=True, null=True, unique=True) 



    date_of_birth = models.DateTimeField(default=datetime.now, blank=True)

    profile_url = models.CharField(max_length=1024, blank=True, null=True, default= "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png")


    def __unicode__(self):
        return f"{self.first_name} {self.last_name}"

    # def __str__(self):
    #     return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        if not self.uuid:
            temp_uuid = str(uuid.uuid4())[:30]
            while User.objects.filter(uuid=temp_uuid).exists():
                temp_uuid = str(uuid.uuid4())[:30]
            self.uuid = temp_uuid


        super().save(*args, **kwargs)
        # user_contact_creation(self)
        # check_upi_setup_event(self)
