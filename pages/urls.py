# from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.urls import include,path

urlpatterns =[
    path('', TemplateView.as_view(template_name='index.html')),

]