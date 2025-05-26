from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, 'landing_page/index.html')


def about(request):
    return render(request, 'landing_page/about.html')


def main(request):
    return render(request, 'landing_page/main.html')


def contact(request):
    return render(request, 'landing_page/contact.html')


def base(request):
    return render(request, 'landing_page/base.html')