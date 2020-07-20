from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    msg = "main페이지 입니다."
    return render(request, 'blog/base.html',{'message': msg})

def post_login(request):
    msg = "login입니다."
    return render(request, 'blog/post_login.html',{'message': msg})

def post_register(request):
    msg="회원가입페이지 입니다~~"
    return render(request, 'blog/post_register.html', {'message': msg})