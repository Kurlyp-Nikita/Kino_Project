from django.contrib import admin
from catalog.models import *
# Register your models here.


admin.site.register(Gener)
admin.site.register(Country)
# admin.site.register(ProfileUser)
# admin.site.register(Actor)
# admin.site.register(Director)


@admin.register(ProfileUser)
class adminProfileUser(admin.ModelAdmin):
    list_display = ('user', 'podpiska', 'balance')  # столбцы в админ панели


@admin.register(Actor)
class adminActor(admin.ModelAdmin):
    list_display = ('name', 'last_name')  # столбцы в админ панели
    list_display_links = ('name', 'last_name') # ссылка на столбец который указан


@admin.register(Director)
class adminDirector(admin.ModelAdmin):
    list_display = ('name', 'last_name')  # столбцы в админ панели
    list_display_links = ('name', 'last_name')  # ссылка на столбец который указан


# admin.site.register(Podpiska)

@admin.register(Kino)
class adminKino(admin.ModelAdmin):
    list_display = ('title', 'gener', 'director', 'year', 'country', 'displayAct')
    fieldsets = (('О фильме', {'fields': ('title', 'gener', 'opisanie')}),
                ('Люди', {'fields': ('director', 'actors')}),
                ('Остальное', {'fields': ('country', 'year', 'podpiska', 'image', 'treler')}))

    list_filter = ('gener', 'podpiska', 'country', 'year')


class PodpiskaLine(admin.StackedInline):
    model = Kino

@admin.register(Podpiska)
class adminPod(admin.ModelAdmin):
    inlines = [PodpiskaLine]


@admin.register(Comment)
class adminComment(admin.ModelAdmin):
    list_display = ('user', 'timedata', 'kino', 'active')  # столбцы в админ панели


