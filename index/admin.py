from django.contrib import admin
from .models import *
from image_cropping import ImageCroppingMixin

class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('category','is_active')
    list_editable = ('is_active',)
    list_display_links = ('category',)

class ImageModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('category','image','img_caption','is_active')
    list_editable = ('category','is_active','img_caption')
    list_display_links = ['image',]

class VideoModelAdmin(admin.ModelAdmin):
    list_display = ('video_caption','video_file')

admin.site.register(Category,CategoryModelAdmin) 
admin.site.register(Image, ImageModelAdmin)
admin.site.register(About)
admin.site.register(Journey)
admin.site.register(Video,VideoModelAdmin)
admin.site.register(Contact)
