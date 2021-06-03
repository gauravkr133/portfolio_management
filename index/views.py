import random
from django.shortcuts import render
from .models import *

context = {}
about_us = About.objects.all()
context['about_us'] = about_us

def index(request):
    slider_img = Image.objects.filter(category=1).filter(is_active=True)
    context['slider_img'] = slider_img

    about_us = About.objects.all()
    context['about_us'] = about_us

    gallery_data = Category.objects.exclude(category="Slider").filter(is_active=True)
    context['gallery_data'] = gallery_data

    video_data = Video.objects.all().filter(is_active=True)[0:4]
    context['video_data'] = video_data

    journey_data = Journey.objects.all().filter(is_active=True)
    context['journey_data'] = journey_data

    event_data = Event.objects.filter(is_active=True)
    context['event_data'] = event_data
    return render(request,"index.html",context)

def about_us(request):
    return render(request,"about_us.html",context)

def gallery(request):
    gallery_data = Category.objects.exclude(category="Slider").filter(is_active=True)
    context['gallery_data'] = gallery_data
    return render(request,"gallery.html",context)

def gallery_detail(request,category):
    img_category_id = Category.objects.filter(category=category).first().id
    category_filter_img = Image.objects.filter(category=img_category_id,is_active=True)
    context['category_filter_img'] = category_filter_img
    return render(request,"gallery_detail.html",context)

def videos(request):
    video_data = Video.objects.all().filter(is_active=True)
    context['video_data'] = video_data
    return render(request,"videos.html",context)

def press(request,type):
    type = type.lower()
    press_data = Press.objects.filter(type=type,is_active=True)
    context['press_data'] = press_data
    return render(request,"press.html",context)

def press_detail(request,id):
    press_data_single = Press.objects.filter(id=id)
    print(press_data_single)
    context['press_data_single'] = press_data_single
    return render(request,"press_detail.html",context) 

def contact_us(request):
    context['msg'] = ""
    context['msg_type'] = ""
    if request.POST:
        first_name = request.POST.get('name')
        last_name  = request.POST.get('surname')
        email      = request.POST.get('email')
        subject    = request.POST.get('subject')
        message    = request.POST.get('message')
        if(first_name and last_name and email and subject and message):
            contact_details = Contact(first_name=first_name,last_name=last_name,email_id=email,subject=subject,message=message)
            contact_details.save()
            context['msg'] = "Thank you for contacting us"
            context['msg_type'] = "success"
            return render(request,"contact_us.html",context)
        else:
            context['msg'] = "Please fill out all the details"
            context['msg_type'] = "danger"
    return render(request,"contact_us.html",context)
