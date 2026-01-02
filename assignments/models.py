from django.db import models

# Create your models here.
class About(models.Model):
  about_heading = models.CharField(max_length=25)
  about_description = models.TextField(max_length=300)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.about_heading
  
  class Meta:
    verbose_name_plural = "About"
    
class Social_Media(models.Model):
  platform_name = models.CharField(max_length=25)
  platform_link = models.URLField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.platform_name