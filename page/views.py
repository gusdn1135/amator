from django.shortcuts import render
from .models import Notice

# Create your views here.
def home(request):
    return render(request, "home.html")

def community(request):
    notices = Notice.objects.all()
    return render(request, 'community.html', {'notices': notices})