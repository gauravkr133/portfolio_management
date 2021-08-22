from django.db import models
from datetime import datetime
from django.utils.text import slugify 
from tinymce.models import HTMLField 

class Blogcategory(models.Model):
	category_id 	= models.AutoField(primary_key=True)
	blog_category 	= models.CharField(max_length=50)
	is_active 		= models.BooleanField(default=True)
	def __str__(self):
		return self.blog_category
		
	def __unicode(self):
		return self.blog_category

class Blogpost(models.Model):
	post_id       = models.AutoField(primary_key=True)
	post_title    = models.CharField(max_length=50)
	post_slug     = models.SlugField(blank=True)
	post_category = models.ManyToManyField(Blogcategory,blank=True)
	post_body     = HTMLField()
	pub_date      = models.DateField(default=datetime.now)
	thumbnail     = models.ImageField(upload_to='images/', default="",blank=True)
	is_active     = models.BooleanField(default=True)

	def save(self, *args, **kwargs):
		all_post = Blogpost.objects.values('post_slug')
		if(self.post_slug=="" or self.post_slug in all_post):
			self.post_slug = slugify(self.post_title)
		super(Blogpost,self).save(*args, **kwargs)
	
	def __str__(self):
		return self.post_title

