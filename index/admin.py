from django.contrib import admin
from .models import *
from image_cropping import ImageCroppingMixin

class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('category','is_active')
    list_editable = ('is_active',)
    list_display_links = ('category',)

class ImageModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('id','category','image','img_caption','is_active')
    list_editable = ('category','is_active','img_caption')
    list_display_links = ['image',]

class VideoModelAdmin(admin.ModelAdmin):
    list_display = ('video_caption','video_file')

class PressModelAdmin(admin.ModelAdmin):
    list_display = ('type','video_caption','press_heading','created_at')

class EventModelAdmin(admin.ModelAdmin):
    list_display = ('event_heading','event_venue','event_date')


admin.site.register(Category,CategoryModelAdmin) 
admin.site.register(Image, ImageModelAdmin)
admin.site.register(About)
admin.site.register(Journey)
admin.site.register(Video,VideoModelAdmin)
admin.site.register(Press,PressModelAdmin)
admin.site.register(Event,EventModelAdmin)
admin.site.register(Contact)
