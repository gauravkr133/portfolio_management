from django.contrib import admin
from .models import *
from image_cropping import ImageCroppingMixin

class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('id','category','is_active','is_dropdown')
    list_editable = ('is_active','is_dropdown')
    list_display_links = ('category',)

class ImageModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('id','category','image','img_caption','is_active')
    list_editable = ('category','is_active','img_caption')
    list_display_links = ['id','image']

class VideoModelAdmin(admin.ModelAdmin):
    list_display = ('id','video_caption','video_file')

class PressModelAdmin(admin.ModelAdmin):
    list_display = ('id','press_heading','created_at')

class EventModelAdmin(admin.ModelAdmin):
    list_display = ('id','event_heading','event_venue','event_start_date','event_end_date')

class VolunteerModelAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','email','phone_number')

class GetInvolveModelAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','phone_number','event_id')


admin.site.register(Category,CategoryModelAdmin) 
admin.site.register(Image, ImageModelAdmin)
admin.site.register(About)
admin.site.register(Journey)
admin.site.register(Video_category)
admin.site.register(Video,VideoModelAdmin)
admin.site.register(Press_category)
admin.site.register(Press,PressModelAdmin)
admin.site.register(Event,EventModelAdmin)
admin.site.register(Contact)
admin.site.register(Volunteer,VolunteerModelAdmin)
admin.site.register(GetInvolve,GetInvolveModelAdmin)

