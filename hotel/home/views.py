from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, Http404
from .models import City,Hotels
from django.template import loader
from django.db.models import Q

# Create your views here.
def index(request):
    cities = City.objects.all()
    template = loader.get_template('home/index.html')
    context = { 'cities':cities}
    return render(request,'home/index.html', context)

def city(request,city_id):
    try:
        cities=City.objects.get(pk=city_id)
    except City.DoesNotExist:
        raise Http404('City does not exist')
    return render(request,'home/city.html',{'cities':cities})

def book(request,city_id):
    return render(request,'home/book.html')

def user_details(request,city_id):
    return render(request,'home/user_details.html')

def confirmation(request):
    return render(request,'home/confirmation.html')

def search(request):
    template = 'home/city.html'
    query = request.GET.get('q')
    results = Post.objects.filter(Q(hotel=query))
