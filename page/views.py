from django.shortcuts import render
from .models import Notice

# Create your views here.
def home(request):
    return render(request, "home.html")

def notice(request):
    notices = Notice.objects.all()
    return render(request, 'notice.html', {'notices': notices})