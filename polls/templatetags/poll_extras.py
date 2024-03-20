import enum

from django import template
from django.urls import reverse
from pprint import pprint
from Menu.models import Menu
from User.models import User
from jalali_date import date2jalali,datetime2jalali

from utils import config_items

register = template.Library()


@register.filter
def getName(user: User):
    if (len(user.first_name) == 0 and len(user.last_name) == 0):
        return user.email
    else:
        return user.first_name + " " + user.last_name


@register.filter
def ActiveClass(value,url):
    in_url=reverse(value)
    if (in_url==url):
        return 'active'

@register.filter
def jalali_date(value):
    return datetime2jalali(value).strftime(' تاریخ   %Y/%m/%d  ساعت  %H:%M:%S')

@register.filter
def jalali_date_cu(value):
    return datetime2jalali(value).strftime(' %d %B %Y')
@register.filter
def getPlace(val):
    for elm in Menu.placeMenu:
        if (val==elm.value):
            return elm.label
            break
@register.filter
def jalali_date_month(value):
    return datetime2jalali(value).strftime(' %B %Y')
@register.filter
def showCat(value):
    return (' و '.join(list(value.values_list('title', flat=True))))
def showTag(value):
    return (' | '.join(list(value.values_list('title', flat=True))))