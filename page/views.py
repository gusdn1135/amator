from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate
from .models import Notice, Account, IndivAcc, TeamAcc, OrgAcc, League
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == 'POST':

        user_id = request.POST['id']
        user_pw = request.POST['pw']

        if(Account.objects.filter(id=user_id).exists()):
            if(Account.objects.filter(pw=user_pw).exists()):
                request.session['user'] = user_id
                return redirect('home')
            else:
                messages.error(request, '비밀번호 오류!')
        else:
            messages.error(request, '아이디 오류!')

    return render(request, 'login.html')

def home(request):
    return render(request, "home.html")

def team(request):
    return render(request, 'team.html')

def signup_agreement(request):
    if request.method == 'POST':
        if(request.POST['agree1'] == '동의' and request.POST['agree2'] == '동의'):
            return redirect('signup_type')
    return render(request, 'signup_agreement.html')


def signup_type(request):
    if request.method == 'POST':
        if(request.POST['id_type'] == 'indiv'):
            return redirect('signup_indiv')
        elif(request.POST['id_type'] == 'team'):
            return redirect('signup_team')
    return render(request, 'signup_type.html')


def signup_indiv(request):
    if request.method == 'POST':
        if(request.POST['pw'] == request.POST['confirm']):
            account = Account(id = request.POST['id'], pw = request.POST['pw'])
            account.save()
            
            indivAcc = IndivAcc(id = Account.objects.get(id=request.POST['id']), indiv_name = request.POST['name'], indiv_studentid = request.POST['studentID'], 
            indiv_belong=request.POST['belong'], indiv_sex= request.POST['sex'], indiv_bdate= request.POST['bdate'],
            indiv_address= request.POST['address'], indiv_pnumber= request.POST['pnumber'], indiv_email= request.POST['email'])
            indivAcc.save()
            
            return redirect('home')

    return render(request, 'signup_indiv.html')

def signup_team(request):
    if request.method == 'POST':
        if(request.POST['pw'] == request.POST['confirm']):
            account = Account(id = request.POST['id'], pw = request.POST['pw'])
            account.save()
            
            teamAcc = TeamAcc(id = Account.objects.get(id=request.POST['id']), team_name = request.POST['team_name'],
            team_belong = request.POST['team_belong'], cap_name = request.POST['cap_name'],
            cap_eamil = request.POST['cap_email'], cap_pnumber = request.POST['cap_pnumber'])
            teamAcc.save()

            return redirect('home')
    

    return render(request, 'signup_team.html')

def league_temp(request):
    if request.method == 'POST':
        # 현재 접속중인 계정 정보 받아오기
        current_account = request.session['user']
        if(OrgAcc.objects.filter(id=current_account).exists()):
            print('주최자 계정 접속 성공! 곧 리그 만들어드림!')
            league = League(id = OrgAcc.objects.get(id=current_account), league_name=request.POST['league_name'],
            league_date=request.POST['league_date'], league_location=request.POST['league_location'])
            league.save()
            print(league.leaguecode)
            # 리그 생성 성공 시 임시로 home으로 redirect
            return redirect('home')

        else:
            messages.error(request, '주최자 계정이 아닙니다!')
    return render(request, 'league_temp.html')


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
