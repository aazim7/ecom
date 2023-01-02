from django.db import models
from base.model import BaseModel
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver



class Profile(BaseModel):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
	is_email_verified = models.BooleanField(default=False)
	email_token = models.CharField(max_length=100, null=True, blank =True)
	profile_image = models.ImageField(upload_to = "profile")

	def __str__(self):
		return str(self.user.first_name)

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, is_email_verified=True)
  
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
        instance.profile.save()