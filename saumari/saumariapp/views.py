from django.shortcuts import render
from django.http import Http404
from .models import Listing, Type


def index(request):
    listings = Listing.objects.all()
    context = {'listings': listings}
    return render(request, 'saumariapp/index.html', context)

def detail(request, listing_id):
    try:
        listing = Listing.objects.get(pk=listing_id)
    except Listing.DoesNotExist:
        raise Http404("Listing does not exist")
    return render(request, 'saumariapp/detail.html', {'listing': listing})

def parandustood(request):
    listings = Listing.objects.all()
    types = Type.objects.all()
    context = {'listings': listings, 'types': types}
    return render(request, 'saumariapp/parandustood.html', context)
