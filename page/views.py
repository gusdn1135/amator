from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate
from .models import Notice, Pr, Account

# Create your views here.
def login(request):
    return render(request, 'login.html')

def home(request):
    return render(request, "home.html")

def team(request):
    return render(request, 'team.html')

def signup(request):
    return render(request, 'signup.html')

def community_notice(request):
    notices = Notice.objects.all()
    return render(request, 'community_notice.html', {'notices': notices})

def community_pr(request):
    prs = Pr.objects.all()
    author = Account.objects.all()
    return render(request, 'community_pr.html', {'prs':prs})

def community_chat(request):
    return render(request, 'community_chat.html')

def community_notice_detail(request, notice_id):
    notice_detail = get_object_or_404(Notice, pk=notice_id)

    return render(request, 'community_notice_detail.html', {'notice': notice_detail})

def community_pr_detail(request, pr_id):
    pr_detail = get_object_or_404(Pr, pk=pr_id)

    return render(request, 'community_pr_detail.html', {'pr': pr_detail})

def login_view(request):
    if request.method == "POST":
        username = request.POST("id")
        password = request.POST("pw")
        user = authenticate(username=username, password=password)
        if user is not None:
            print("인증성공")
        else:
            print("인증실패")
    return render(request, "logini.html")
