import random
from django.shortcuts import render,redirect
from .models import *
from blog.models import *
from django.http import JsonResponse

context = {}
about_us = About.objects.all()
context['about_us'] = about_us

def index(request):
    slider_img = Image.objects.filter(category__category__contains="Slider").filter(is_active=True)
    context['slider_img'] = slider_img

    about_us = About.objects.all()
    context['about_us'] = about_us

    category_data = Category.objects.exclude(category="Slider").filter(is_active=True)
    context['category_data'] = category_data

    img_data = Image.objects.exclude(category__category__contains="Slider").filter(is_active=True)
    context['img_data'] = img_data
    
    video_data = Video.objects.all().filter(is_active=True)[0:4]
    context['video_data'] = video_data

    journey_data = Journey.objects.all().filter(is_active=True)
    context['journey_data'] = journey_data

    event_data = Event.objects.filter(is_active=True)
    context['event_data'] = event_data

    new_initiative_data = Event.objects.filter(is_active=True,is_new_initiative=True)
    context['initiative_data'] = new_initiative_data

    blog_data = Blogpost.objects.filter(is_active=True).order_by('-post_id')[:3]
    context['blog_data'] = blog_data
    
    if request.is_ajax():
        if request.POST:
            first_name = request.POST.get('name')
            last_name  = request.POST.get('surname')
            email      = request.POST.get('email')
            subject    = request.POST.get('subject')
            message    = request.POST.get('message')
            if(first_name and last_name and email and subject and message):
                contact_details = Contact(first_name=first_name,last_name=last_name,email_id=email,subject=subject,message=message)
                contact_details.save()
                return JsonResponse({'message':'Success'})
                
    return render(request,"index.html",context)

def about_us(request):
    return render(request,"about_us.html",context)

def gallery(request):
    gallery_data = Category.objects.exclude(category="Slider").filter(is_active=True)
    context['gallery_data'] = gallery_data
    return render(request,"gallery.html",context)

def gallery_detail(request,category):
    try:
        img_category_id = Category.objects.filter(category=category).first().id
        category_filter_img = Image.objects.filter(category=img_category_id,is_active=True)
        context['category_filter_img'] = category_filter_img
    except:
        return redirect('gallery')
    return render(request,"gallery_detail.html",context)

def videos(request):
    video_data = Video.objects.all().filter(is_active=True)
    context['video_data'] = video_data
    return render(request,"videos.html",context)

def event_details(request,event_heading,event_id):
    event_data = Event.objects.filter(id=event_id,event_heading=event_heading)
    context['event_data'] = event_data
    return render(request,"event_details.html",context)

def press(request,type):
    type = type.lower()
    try:
        press_data = Press.objects.filter(type=type,is_active=True)
        context['press_data'] = press_data
    except:
        return redirect('index')
    return render(request,"press.html",context)

def press_detail(request,id):
    try:
        press_data_single = Press.objects.filter(id=id)
        context['press_data_single'] = press_data_single
    except:
        return redirect('index')
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

def volunteer(request):
    if request.is_ajax():
        if request.POST:
            first_name      = request.POST.get('firstname')
            last_name       = request.POST.get('lastname')
            email           = request.POST.get('email')
            phone_number    = request.POST.get('phone_number')
            address         = request.POST.get('address')
            city            = request.POST.get('city')
            state           = request.POST.get('state')
            about           = request.POST.get('about')
            if(first_name and last_name and email and phone_number and address and city and state and about):
                Volunteer_details = Volunteer(first_name=first_name,last_name=last_name,email=email,phone_number=phone_number,address=address,city=city,state=state,about=about)
                Volunteer_details.save()
                return JsonResponse({'message':'Success'})
    return render(request,"volunteer.html",context)
    

def get_involve(request):
    event_data = Event.objects.filter(is_active=True)
    context['event_data'] = event_data
    if request.is_ajax():
        if request.POST:
            first_name      = request.POST.get('firstname')
            last_name       = request.POST.get('lastname')
            event_id        = request.POST.get('event_id')
            event_inst      = Event.objects.get(id=event_id)
            phone_number    = request.POST.get('phone_number')
            about           = request.POST.get('about')
            if(first_name and last_name and event_id and phone_number and about):
                get_involve_details = GetInvolve(first_name=first_name,last_name=last_name,event_id=event_inst,phone_number=phone_number,about=about)
                get_involve_details.save()
                return JsonResponse({'message':'Success'})
    return render(request,"get_involve.html",context)

def view_400(request,exception):
    return render(request,"400.html")

def view_403(request,exception):
    return render(request,"403.html")

def view_404(request,exception):
    return render(request,"404.html")

def view_500(request):
    return render(request,"500.html")
