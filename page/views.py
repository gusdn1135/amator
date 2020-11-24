from django.shortcuts import render
from .models import Notice

# Create your views here.
def home(request):
    return render(request, "home.html")

def team(request):
    return render(request, 'team.html')

def community_notice(request):
    notices = Notice.objects.all()
    return render(request, 'community_notice.html', {'notices': notices})