from django.db import models
from django.db.models.enums import Choices
from image_cropping import ImageRatioField
from froala_editor.fields import FroalaField

class Category(models.Model):
    id                  = models.AutoField(primary_key=True)
    category            = models.CharField(max_length = 100)
    category_thumbnail  = models.ImageField(upload_to='images/',blank=True)
    is_active           = models.BooleanField(default=True)

    def __str__(self):
        return self.category

class Image(models.Model):
    id          = models.AutoField(primary_key=True)
    category    = models.ForeignKey(Category,on_delete = models.CASCADE,blank=True)
    image       = models.ImageField(upload_to='images/')
    cropping    = ImageRatioField('image', '430x360')
    img_caption = models.CharField(max_length = 100)
    is_active   = models.BooleanField(default=True)

    def __str__(self):
        return self.img_caption

class About(models.Model):
    id                  = models.AutoField(primary_key=True)
    heading             = models.CharField(max_length = 100)
    about_thumbnail     = models.ImageField(upload_to='images/',blank=True)
    short_description   = models.TextField(blank=True)
    description         = FroalaField()
    name                = models.CharField(max_length = 100,blank=True,null=True)
    location            = models.CharField(max_length = 100,blank=True,null=True)
    phone_number        = models.CharField(max_length =15,blank=True,null=True)
    email_id            = models.EmailField(max_length = 100,blank=True,null=True)
    social_facebook     = models.URLField(max_length = 500,blank=True,null=True)
    social_twitter      = models.URLField(max_length = 500,blank=True,null=True)
    social_youtube      = models.URLField(max_length = 500,blank=True,null=True)
    social_instagram    = models.URLField(max_length = 500,blank=True,null=True)
    wikipedia           = models.URLField(max_length = 500,blank=True,null=True)
    def __str__(self):
        return self.heading


class Journey(models.Model):
    id = models.AutoField(primary_key=True)
    date        = models.DateField(blank=True,help_text = "Please use the following format: <em>YYYY-MM-DD</em>.")
    heading     = models.CharField(max_length = 100,blank=True)
    description = models.TextField(max_length=500)
    is_active   = models.BooleanField(default=True)
    def __str__(self):
        return self.heading

class Video(models.Model):
    id              = models.AutoField(primary_key=True)
    video_caption   = models.CharField(max_length = 100)
    video_thumbnail = models.ImageField(upload_to='images/',blank=True)
    video_file      = models.FileField(upload_to='videos/',blank=True,null=True)
    video_code      = models.CharField(max_length = 100,blank=True,null=True)
    is_active       = models.BooleanField(default=True)
    def __str__(self):
        return self.video_caption

class Contact(models.Model):
    id         = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length = 100)
    last_name  = models.CharField(max_length = 100)
    email_id   = models.EmailField(max_length = 100)
    subject    = models.CharField(max_length = 200)
    message    = models.TextField(max_length=500)
    def __str__(self):
        return self.first_name

PRESS_CHOICES = (
    ('news','news'),
    ('editorials','editorials'),
    ('interviews','interviews'),
    ('critics','critics'),
    ('press releases','press releases')
)
class Press(models.Model):
    id                  = models.AutoField(primary_key=True)
    type                = models.CharField(max_length=100,choices=PRESS_CHOICES)
    video_caption       = models.CharField(max_length = 100,blank=True)
    video_thumbnail     = models.ImageField(upload_to='images/',blank=True)
    video_file          = models.FileField(upload_to='videos/',blank=True,null=True)
    video_code          = models.CharField(max_length = 100,blank=True,null=True,help_text="Enter only video code of youtube video")
    press_heading       = models.CharField(max_length=300,blank=True, null=True)
    press_description   = models.TextField(max_length=1000,blank=True)
    created_at          = models.DateField(help_text = "Please use the following format: <em>YYYY-MM-DD</em>.")
    is_active           = models.BooleanField(default=True)
    def __str__(self):
        return self.type

class Event(models.Model):
    id                  = models.AutoField(primary_key=True)
    event_poster        = models.ImageField(upload_to='images/',blank=True)
    event_heading       = models.CharField(max_length=200,blank=True)
    event_description   = models.TextField(max_length=1000,blank=True)
    event_venue         = models.CharField(max_length=150,blank=True)
    event_date          = models.DateField(auto_now_add=True)
    is_active           = models.BooleanField(default=True)
    def __str__(self):
        return self.event_heading