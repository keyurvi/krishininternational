from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.mail import send_mail
from django.http import HttpResponse # Add this
from django.conf import settings

from .forms import ContactUsForm # Add this

def index(request):
    form = ContactUsForm()
    return render(request, 'index.html', {'form': form})

def about_us(request):
    return render(request, 'about-us.html')

def products(request):
    return render(request, 'products.html')

def why_choose_us(request):
    return render(request, 'why-choose-us.html')

def globle_footprint(request):
    return render(request, 'global_footprint.html')

def contact__us(request):
    return render(request, 'contact_us.html')

def wcutbag(request):
    return render(request, 'w-cut-bag.html')

def non_woven_fabric(request):
    return render(request, 'non-woven-fabric.html')

def sack_bags(request):
    return render(request, 'sack-bags.html')

def wine_bags(request):
    return render(request, 'wine-bags.html')

def loop_handle_bag(request):
    return render(request, 'loop-handle-bag.html')

def leno_mesh_bag(request):
    return render(request, 'leno-mesh-bag.html')

def jumbo_fibc_bag(request):
    return render(request, 'jumbo-fibc-bag.html')

def d_cut_bag(request):
    return render(request, 'd-cut-bag.html')

def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            # send email code goes here
            sender_name = form.cleaned_data['name']
            sender_number = form.cleaned_data['phone_number']
            sender_email = form.cleaned_data['email']
            email_from = settings.EMAIL_HOST_USER
            message = "{0} has sent you a new message.\n\nPhone Number : {1}\n\nEmail : {2}\n\nMessage : {3}".format(sender_name,sender_number, sender_email, form.cleaned_data['message'])
            send_mail('New Enquiry', message, email_from, ['krishinint@gmail.com'])
            form.save()
            return redirect("/")
    else:
        form = ContactUsForm()

    return render(request, 'index.html', {'form': form})
# Create your views here.
