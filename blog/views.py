from django.shortcuts import render
from django.http import HttpResponse
# 여긴 메인 홈 입니다.
def about(request):
    return HttpResponse("이 페이지는 about 페이지 입니다.")