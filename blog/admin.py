from django.contrib import admin
from .models import *


class BlogpostModelAdmin(admin.ModelAdmin):
    readonly_fields = ('post_slug',)
    list_display = ['post_id','post_title','post_slug','pub_date','is_active']
    list_editable = ('post_title','is_active')

admin.site.register(Blogpost,BlogpostModelAdmin)
admin.site.register(Blogcategory)