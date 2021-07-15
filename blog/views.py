from django.shortcuts import render
from index.models import *
from .models import *
from django.db.models import Count


context = {}
def nav_data():
    about_us = About.objects.all()
    context['about_us'] = about_us

    gallery_dropdown_data = Category.objects.filter(is_dropdown=True)
    context['gallery_dropdown_data'] = gallery_dropdown_data

    press_dropdown_data = Press_category.objects.filter(is_dropdown=True)
    context['press_dropdown_data'] = press_dropdown_data

    video_dropdown_data = Video_category.objects.filter(is_dropdown=True)
    context['video_dropdown_data'] = video_dropdown_data


def blog(request):
    nav_data()
    about_us = About.objects.all()
    context['about_us'] = about_us

    latest_blog_data = Blogpost.objects.filter(is_active=True).order_by('-post_id')[:4]
    context['latest_blog_data'] = latest_blog_data

    category_data = Blogpost.objects.values('post_category__blog_category').exclude(post_category__isnull=True).annotate(category_count=Count('post_category'))
    context['category_data'] = category_data

    dropdown_data = Category.objects.filter(is_dropdown=True)
    context['dropdown_data'] = dropdown_data

    blog_data = Blogpost.objects.filter(is_active=True)
    context['blog_data'] = blog_data
    return render(request,"blog.html",context)

def blog_detail(request,slug):
    nav_data()
    blog_detail = Blogpost.objects.filter(post_slug=slug,is_active=True)
    context['blog_detail'] = blog_detail
    return render(request,"blog_detail.html",context)

def category_detail(request,category_name=None):
    nav_data()
    if category_name != None:
        category_id = Blogcategory.objects.values('category_id').filter(blog_category=category_name)
        blog_data = Blogpost.objects.filter(post_category__category_id__contains=category_id,is_active=True)
    else:
        blog_data = Blogpost.objects.filter(is_active=True)

    context['blog_data'] = blog_data

    return render(request,"blog.html",context)
