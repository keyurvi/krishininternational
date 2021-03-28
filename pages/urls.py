# from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.urls import include,path
from .views import *

urlpatterns =[
    path('', index, name='home'),
    path('about-us/', about_us, name='about-us'),
    path('products/', products, name='products'),
    path('why-choose-us/', why_choose_us, name='why-choose-us'),
    path('globle-footprint/',globle_footprint, name='globle-footprint'),
    path('contact-us/',contact__us, name='contact-us'),
    path('w-cut-bag/',wcutbag, name='w-cut-bag'),
    path('save_contact',contact_us),
    # path('', TemplateView.as_view(template_name='index.html')),
]