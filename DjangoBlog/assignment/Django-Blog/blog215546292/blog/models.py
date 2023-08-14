from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

class Article(models.Model):
	title = models.CharField(max_length=255)
	content = HTMLField()
	date = models.DateField(auto_now_add=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	profile_pic=models.ImageField(null=True, blank=True)
	featured = models.BooleanField(default=False)
	likes = models.ManyToManyField(User, related_name='likes', blank=True)
