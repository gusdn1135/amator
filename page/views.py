from django.shortcuts import render, get_object_or_404
from .models import Notice

# Create your views here.
def home(request):
    return render(request, "home.html")

def team(request):
    return render(request, 'team.html')

def community_notice(request):
    notices = Notice.objects.all()
    return render(request, 'community_notice.html', {'notices': notices})

def community_pr(request):
    return render(request, 'community_pr.html')

def community_chat(request):
    return render(request, 'community_chat.html')

def community_notice_detail(request, notice_id):
    notice_detail = get_object_or_404(Notice, pk=notice_id)

    return render(request, 'community_notice_detail.html', {'notice': notice_detail})