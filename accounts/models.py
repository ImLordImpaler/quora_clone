from django.contrib.auth.models import User 
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, null=True , blank=True)
    phone = models.CharField(max_length=10 , null=True , blank=True)
    profile_pic = models.CharField(max_length=100 , null=True , blank=True)  # Upload the photo to AWS S3 Bucket. Paste the reference here
    
    about = models.TextField(blank=True)
    
    def __str__(self):
        return self.name 
    
    
    
@receiver(post_save, sender=User)
def signal_name(sender, instance, created, **kwargs):
    if created: 
        Profile.objects.create(
            name = instance.username,
            user = instance
        )
        