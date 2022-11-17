from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, 'dasmoto_app/index.html')
