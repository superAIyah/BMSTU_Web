from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    phone = models.CharField(max_length=20, default='')
    city = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.first_name

class Autors(models.Model):
    name = models.CharField(max_length=100)
    family_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.family_name}"

class Subjects(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)

class Articles(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to="photos", default="None")
    autor_id = models.ManyToManyField(Autors)
    subject_id = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    photo_link = models.CharField(max_length=100, default="no_link")
    subject = models.CharField(max_length=100, default="no_subject")
    price = models.IntegerField(default=0)
    cart = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)