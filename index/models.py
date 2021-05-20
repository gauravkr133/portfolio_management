from django.db import models
from image_cropping import ImageRatioField
from froala_editor.fields import FroalaField

class Category(models.Model):
    category = models.CharField(max_length = 100)
    category_thumbnail = models.ImageField(upload_to='images/',blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.category

class Image(models.Model):
    category = models.ForeignKey(Category,on_delete = models.CASCADE,blank=True)
    image = models.ImageField(upload_to='images/')
    cropping = ImageRatioField('image', '430x360')
    img_caption = models.CharField(max_length = 100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.img_caption

class About(models.Model):
    heading = models.CharField(max_length = 100)
    about_thumbnail = models.ImageField(upload_to='images/',blank=True)
    short_description = models.TextField(blank=True)
    description = FroalaField()
    name = models.CharField(max_length = 100,blank=True,null=True)
    location = models.CharField(max_length = 100,blank=True,null=True)
    phone_number = models.CharField(max_length = 12,blank=True,null=True)
    email_id = models.EmailField(max_length = 100,blank=True,null=True)
    social_facebook = models.URLField(max_length = 500,blank=True,null=True)
    social_twitter = models.URLField(max_length = 500,blank=True,null=True)
    social_youtube = models.URLField(max_length = 500,blank=True,null=True)
    social_instagram = models.URLField(max_length = 500,blank=True,null=True)
    def __str__(self):
        return self.heading

class Video(models.Model):
    video_caption = models.CharField(max_length = 100)
    video_thumbnail = models.ImageField(upload_to='images/',blank=True)
    video_file = models.FileField(upload_to='videos/',blank=True,null=True)
    video_code = models.CharField(max_length = 100,blank=True,null=True)
    def __str__(self):
        return self.video_caption

class Contact(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name  = models.CharField(max_length = 100)
    email_id   = models.EmailField(max_length = 100)
    subject    = models.CharField(max_length = 200)
    message    = models.TextField(max_length=500)
    def __str__(self):
        return self.first_name
