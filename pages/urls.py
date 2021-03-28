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
    path('non-woven-fabric/',non_woven_fabric, name='non-woven-fabric'),
    path('sack-bags/',sack_bags, name='sack-bags'),
    path('wine-bags/',wine_bags, name='wine-bags'),
    path('loop-handle-bag/',loop_handle_bag, name='loop-handle-bag'),
    path('leno-mesh-bag/',leno_mesh_bag, name='leno-mesh-bag'),
    path('jumbo-fibc-bag/',jumbo_fibc_bag, name='jumbo-fibc-bag'),
    path('d-cut-bag/',d_cut_bag, name='d-cut-bag'),
    path('save_contact',contact_us),
    # path('', TemplateView.as_view(template_name='index.html')),
]