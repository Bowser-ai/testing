from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from lists.models import Item, List


def home_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html')


def new_list(request: HttpRequest) -> HttpResponse:
    new_list_item_text = request.POST['item_text']
    new_list = List.objects.create()
    Item.objects.create(text=new_list_item_text, list=new_list)
    return HttpResponseRedirect(f'/lists/{new_list.id}/')


def view_list(request: HttpRequest, id: int) -> HttpResponse:
    list_ = List.objects.get(id=id)
    context = {
        'list': list_
    }
    return render(request, 'list.html', context)


def add_item(request: HttpRequest, id: int) -> HttpResponse:
    new_list_item_text = request.POST['item_text']
    list_ = List.objects.get(id=id)
    Item.objects.create(text=new_list_item_text, list=list_)
    return HttpResponseRedirect(f'/lists/{id}/')
