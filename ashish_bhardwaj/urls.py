"""ashish_bhardwaj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from froala_editor import views
from index import views as index_views
import index

from blog import views as blog_views

admin.site.site_header  = 'Ashish Bhardwaj'                  
admin.site.index_title  = 'Ashish Bhardwaj'                 
admin.site.site_title   = 'Ashish Bhardwaj Admin' 

handler400 = 'index.views.view_400'
handler403 = 'index.views.view_403'
handler404 = 'index.views.view_404'
handler500 = 'index.views.view_500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('froala_editor/',include('froala_editor.urls')),
    path('',index_views.index, name="index"),
    path('about_us/',index_views.about_us, name="about_us"),
    path('journey/',index_views.journey, name="journey"),
    path('gallery/',index_views.gallery,name="gallery"),
    path('gallery_detail/<str:category>',index_views.gallery_detail,name="gallery_detail"),
    path('videos/<str:video_category>',index_views.videos,name="videos"),
    path('press/<str:press_category>',index_views.press,name="press"),
    path('press_detail/<int:id>',index_views.press_detail,name="press_detail"),
    path('event_details/<str:event_heading>/<int:event_id>',index_views.event_details,name="event_details"),
    path('contact_us/',index_views.contact_us,name="contact_us"),
    path('volunteer/',index_views.volunteer,name="volunteer"),
    path('get_involve/',index_views.get_involve,name="get_involve"),
    path('blog/',blog_views.blog,name="blog"),
    path('blog_detail/<slug:slug>',blog_views.blog_detail,name="blog_detail"),
    path('category/<str:category_name>',blog_views.category_detail,name="category_detail",),
    path('category/',blog_views.category_detail,name="category_detail",),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


