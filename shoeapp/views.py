from django.shortcuts import render
from shoeapp.models import Manufacturer, ShoeType, ShoeColor, Shoe

# Create your views here.
def index(request):
    return render(request, 'index.htm')
