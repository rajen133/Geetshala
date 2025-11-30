from django.shortcuts import render
from django.http import HttpResponse

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)