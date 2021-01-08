from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from . import models
from django.http import Http404

from user.models import User


# Create your views here.

def list(request):
    if hasattr(request, 'session') and 'userinfo' in request.session:
        userId = request.session['userinfo']['userId']
        user = User.objects.get(id=userId)
        print(user)
        notes = models.Note.objects.filter(user=user)
        return render(request, 'list.html', locals())
    else:
        raise Http404


def add(request):
    if request.method == "GET":
        return render(request, 'add.html')
    elif request.method == "POST":
        if hasattr(request, 'session') and 'userinfo' in request.session:
            # 创建note
            title = request.POST.get('title', '')
            content = request.POST.get('content', '')

            userId = request.session['userinfo']['userId']
            user = models.User.objects.get(id=userId)

            note = models.Note.objects.create(
                title=title,
                content=content,
                user=user
            )
            return HttpResponseRedirect('/note/list')
        else:
            raise Http404


def mod(request, note_id):
    pass


def delete(request, note_id):
    pass
