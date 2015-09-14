from django.shortcuts import render
from django.http import Http404
from .models import Listing, Type, Image


def index(request):
    listings = Listing.objects.all()
    context = {'listings': listings}
    return render(request, 'saumariapp/index.html', context)

def detail(request, image_id):
    try:
        image = Image.objects.get(pk=image_id)
    except Image.DoesNotExist:
        raise Http404("Image does not exist")
    return render(request, 'saumariapp/detail.html', {'image': image})

def parandustood(request):
    listings = Listing.objects.all()
    types = Type.objects.all()
    context = {'listings': listings, 'types': types}
    return render(request, 'saumariapp/parandustood.html', context)

def trenniriided(request):
    images = Image.objects.all()
    context = {'images': images}
    return render(request, 'saumariapp/trenniriided.html', context)
