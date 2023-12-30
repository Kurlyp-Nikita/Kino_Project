from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


# class User(AbstractUser):
#     podpiska = models.ForeignKey(Podpiska, on_delete=models.SET_NULL, null=True)


class Gener(models.Model):
    name = models.CharField(max_length=50, verbose_name='жанр')

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    info = models.URLField(blank=True)
    data = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
    filmcount = models.IntegerField(verbose_name='Всего фильмов', blank=True, null=True)
    best = models.TextField(max_length=200, verbose_name='Лучшие фильмы', blank=True, null=True)
    image = models.URLField(verbose_name='Фото', blank=True, null=True)

    def getAbsUrl(self):  # функция создать уникальную ссылку, в данном случае для режисёров
        return reverse('infodirector', args=[self.id])

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    info = models.URLField(blank=True)
    data = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
    filmcount = models.IntegerField(verbose_name='Всего фильмов', blank=True, null=True)
    best = models.TextField(max_length=200, verbose_name='Лучшие фильмы', blank=True, null=True)
    image = models.URLField(verbose_name='Фото', blank=True, null=True)

    def getAbsUrl(self):  # функция создать уникальную ссылку, в данном случае для актёров
        return reverse('infoactor', args=[self.id])

    def __str__(self):
        return self.last_name


class Country(models.Model):
    name = models.CharField(max_length=50, verbose_name='Страна')

    def __str__(self):
        return self.name

class Podpiska(models.Model):
    VIBOR = (('free', 'free'), ('based', 'based'), ('super', 'super'))
    level = models.CharField(max_length=20, choices=VIBOR, verbose_name='Подписка')

    def __str__(self):
        return self.level

class Kino(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    gener = models.ForeignKey(Gener, on_delete=models.SET_NULL, null=True)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    year = models.IntegerField(verbose_name='год выхода')
    actors = models.ManyToManyField(Actor, verbose_name='Актёры')
    podpiska = models.ForeignKey(Podpiska, on_delete=models.SET_NULL, null=True)
    image = models.URLField(verbose_name='Постер', blank=True)
    opisanie  = models.TextField(max_length=50000, verbose_name='Описание')
    treler = models.URLField(verbose_name='Трейлер', blank=True, null=True)

    def __str__(self):
        return self.title

    def displayAct(self):
        res = ''
        for one in self.actors.all():
            res += one.last_name + ', '
        return res

    displayAct.short_description = 'Актёры'

    def getAbsUrl(self):  # функция создать уникальную ссылку, в данном случае для фильмов
        return reverse('infokino', args=[self.id])


class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    podpiska = models.ForeignKey(Podpiska, on_delete=models.SET_NULL, null=True)
    balance = models.IntegerField(default=10)

    # def __str__(self):
    #     return self.user


class Comment(models.Model):
    # name = models.CharField()
    body = models.TextField(verbose_name='Оставьте коментарий')
    timedata = models.DateField(auto_now=True)
    active = models.BooleanField(default=False)
    kino = models.ForeignKey(Kino, on_delete=models.CASCADE)  # CASCADE - команда если удалить фильм, то удаляются комментарии
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
