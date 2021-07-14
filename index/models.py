from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import BigAutoField
from django.db.models.query_utils import PathInfo
from froala_editor.fields import FroalaField
from datetime import datetime    

class Category(models.Model):
    id                    = models.BigAutoField(primary_key=True)
    category              = models.CharField(max_length = 100)
    category_thumbnail    = models.ImageField(upload_to='images/',blank=True)
    is_dropdown           = models.BooleanField(default=False)
    is_active             = models.BooleanField(default=True)

    def __str__(self):
        return self.category

class Image(models.Model):
    id          = models.BigAutoField(primary_key=True)
    category    = models.ForeignKey(Category,on_delete = models.CASCADE,blank=True)
    image       = models.ImageField(upload_to='images/')
    img_caption = models.CharField(max_length = 100)
    is_active   = models.BooleanField(default=True)

    def __str__(self):
        return self.img_caption

class About(models.Model):
    id                  = models.BigAutoField(primary_key=True)
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
    koo                 = models.URLField(max_length = 500,blank=True,null=True)
    def __str__(self):
        return self.heading


class Journey(models.Model):
    id          = models.BigAutoField(primary_key=True)
    date        = models.DateField(blank=True,help_text = "Please use the following format: <em>YYYY-MM-DD</em>.")
    heading     = models.CharField(max_length = 100,blank=True)
    description = FroalaField()
    is_active   = models.BooleanField(default=True)
    def __str__(self):
        return self.heading

class Video_category(models.Model):
    id                    = models.BigAutoField(primary_key=True)
    video_category        = models.CharField(max_length = 100)
    is_dropdown           = models.BooleanField(default=False)
    is_active             = models.BooleanField(default=True)

    def __str__(self):
        return self.video_category

class Video(models.Model):
    id              = models.BigAutoField(primary_key=True)
    category        = models.ForeignKey(Video_category,on_delete = models.CASCADE,blank=True,null=True)
    video_caption   = models.CharField(max_length = 100)
    video_thumbnail = models.ImageField(upload_to='images/',blank=True)
    video_file      = models.FileField(upload_to='videos/',blank=True,null=True)
    video_code      = models.CharField(max_length = 100,blank=True,null=True)
    is_active       = models.BooleanField(default=True)
    def __str__(self):
        return self.video_caption

class Contact(models.Model):
    id         = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length = 100)
    last_name  = models.CharField(max_length = 100)
    email_id   = models.EmailField(max_length = 100,blank=True)
    subject    = models.CharField(max_length = 200)
    message    = models.TextField(max_length=500)
    def __str__(self):
        return self.first_name



class Press_category(models.Model):
    id                    = models.BigAutoField(primary_key=True)
    press_category        = models.CharField(max_length = 100)
    is_dropdown           = models.BooleanField(default=False)
    is_active             = models.BooleanField(default=True)
    def __str__(self):
        return self.press_category

class Press(models.Model):
    id                  = models.BigAutoField(primary_key=True)
    category            = models.ForeignKey(Press_category,on_delete = models.CASCADE,blank=True,null=True)
    press_thumbnail     = models.ImageField(upload_to='images/',blank=True)
    press_heading       = models.CharField(max_length=300,blank=True, null=True)
    press_description   = FroalaField()
    created_at          = models.DateField(help_text = "Please use the following format: <em>YYYY-MM-DD</em>.")
    is_active           = models.BooleanField(default=True)
    def __str__(self):
        return self.press_heading

class Event(models.Model):
    id                          = models.BigAutoField(primary_key=True)
    event_poster                = models.ImageField(upload_to='images/',blank=True)
    event_heading               = models.CharField(max_length=200,blank=True)
    event_description           = FroalaField()
    event_venue                 = models.CharField(max_length=150,blank=True)
    event_start_date            = models.DateTimeField(default=datetime.now)
    event_end_date              = models.DateTimeField(default=datetime.now)
    is_new_initiative           = models.BooleanField(default=False)
    is_active                   = models.BooleanField(default=True)
    def __str__(self):
        return self.event_heading

class Volunteer(models.Model):
    id              = models.BigAutoField(primary_key=True)
    first_name      = models.CharField(max_length=100,blank=True)
    last_name       = models.CharField(max_length=100,blank=True)
    email           = models.EmailField(max_length=200,blank=True)
    phone_number    = models.CharField(max_length =15,blank=True)
    address         = models.CharField(max_length=300,blank=True)
    city            = models.CharField(max_length=100,blank=True)
    state           = models.CharField(max_length=100,blank=True)
    about           = models.TextField(max_length=500,blank=True)
    def __str__(self):
        return self.first_name

class GetInvolve(models.Model):
    id              = models.BigAutoField(primary_key=True)
    first_name      = models.CharField(max_length=100,blank=True)
    last_name       = models.CharField(max_length=100,blank=True)
    event_id        = models.ForeignKey(Event, on_delete=models.CASCADE)
    phone_number    = models.CharField(max_length =15,blank=True)
    about           = models.TextField(max_length=500,blank=True)
    def __str__(self):
        return self.first_name

