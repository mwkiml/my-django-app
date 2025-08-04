from django.shortcuts import render
from django.http import HttpResponse
# 여긴 메인 홈 입니다.
def home(request):
    return HttpResponse("Hello from the blog app!")