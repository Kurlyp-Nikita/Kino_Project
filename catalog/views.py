from django.shortcuts import render, redirect
from django.views import generic  # функция генерации чего-то
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def index(req):
    items = Kino.objects.all()
    items2 = Kino.objects.filter(podpiska__level='free')
    data = {'k1': items.count(), 'k2': items2.count()}
    return render(req, 'index.html', data)


class kinolist(generic.ListView):
    model = Kino
    paginate_by = 5

# class kinodetail(generic.DetailView):
#     model = Kino


def proverka(newcom):
    blacklist = ['блять']
    spisok = newcom.body.split()

    if any(one in blacklist for one in spisok):
        newcom.delete()
    else:
        newcom.active = True
        newcom.save()



def kinodetail(req, pk):
    film = Kino.objects.get(id=pk)
    comments = film.comment_set.filter(active=True)
    forma = CommentForm()
    if req.POST:
        newcom = Comment()
        newcom.body = req.POST.get('body')
        newcom.kino = film
        newcom.user = req.user
        newcom.save()
        proverka(newcom)

    data = {'kino': film, 'form': forma, 'comments': comments}
    return render(req, 'catalog/kino_detail.html', data)


class directorlist(generic.ListView):
    model = Director
    paginate_by = 5

class directordetail(generic.DetailView):
    model = Director


class actorlist(generic.ListView):
    model = Actor

class actordetail(generic.DetailView):
    model = Actor


def reg(req):
    # return redirect('home')
    if req.POST:  # условие для правильной регистирации
        forma = SignUp(req.POST)
        if forma.is_valid():  # is_valid() - функция проверки
            forma.save()

            #  достаём данные из формы(пользователя)
            k1 = forma.cleaned_data.get('username')
            k2 = forma.cleaned_data.get('password1')
            k3 = forma.cleaned_data.get('email')
            k4 = forma.cleaned_data.get('first_name')
            k5 = forma.cleaned_data.get('last_name')

            #  создаём нового пользователя
            user = authenticate(username=k1, password=k2)
            newuser = User.objects.get(username=k1)  # находим нашего пользователя

            # заполняем поля пользователя
            newuser.email = k3
            newuser.first_name = k4
            newuser.last_name = k5
            newuser.save()
            ProfileUser.objects.create(user_id=newuser.id, podpiska_id=1)  # создаёт запись в ProfileUser, подписка free автоматом для нового пользователя
            login(req, user)

            return redirect('home')

    else:  # условие для регистрации
        forma = SignUp()  # это если 1-й раз зашёл, отправляется форма для заполнения

    data = {'forma': forma}
    return render(req, 'registration/registration.html', data)


def topodpiska(req, userid):
    data = {}

    if req.POST:
        print(userid)
        print('ok1')

        if req.POST.get('stype'):

            stype = req.POST.get('stype')
            print(stype)
            user = User.objects.get(id=userid)
            newpod = Podpiska.objects.get(level=stype)

            if stype == 'free':
                user.profileuser.podpiska = newpod

            elif stype == 'based' and user.profileuser.balance >= 1:
                user.profileuser.balance -= 1
                user.profileuser.podpiska = newpod

            elif stype == 'super' and user.profileuser.balance >= 5:
                user.profileuser.balance -= 5
                user.profileuser.podpiska = newpod

            user.profileuser.save()

        elif req.POST.get('summa'):
            summa = req.POST.get('summa')
            print(summa)
            user = User.objects.get(id=userid)
            user.profileuser.balance += int(summa)
            user.profileuser.save()

    return render(req, 'podpiska.html', data)


# def plusbalance(req):
#     data = {}
#     return redirect('podpiska')
