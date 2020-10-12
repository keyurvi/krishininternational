# from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.urls import include,path
from .views import index,contact_us

urlpatterns =[
    path('', index),
    path('save_contact',contact_us),
    # path('', TemplateView.as_view(template_name='index.html')),
]