from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from . import models

# Create your views here.


def logout(request):
    if request.method == 'GET':
        del request.session['userinfo']
        return HttpResponseRedirect('/')


def login(request):
    if request.method == "GET":
        return render(request, 'login.html', locals())

    elif request.method == 'POST':
        username = request.POST.get('username', '')
        pwd = request.POST.get('password', '')

        try:
            # 找到用户
            user = models.User.objects.get(username=username)
            if pwd == user.password:
                request.session['userinfo'] = {
                    'username': username,
                    'userId': user.id
                }
                return HttpResponseRedirect('/')
            else:
                return HttpResponse('密码错误')

        except:
            return HttpResponse('用户名密码错误')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html', locals())
    elif request.method == 'POST':
        # 获取注册的用户名密码
        username = request.POST.get('username', '')
        pwd = request.POST.get('password', '')

        # 校验用户名密码的正确性
        if not username:
            name_error = '用户名不能为空'
            return render(request, 'register.html', locals())
        elif not pwd:
            pwd_error = '密码不能为空'
            return render(request, 'register.html', locals())
        else:
            # 数据库创建对应的用户
            models.User.objects.create(username=username, password=pwd)

            # 返回注册成功
            return render(request, 'user/templates/login.html')
