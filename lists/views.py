from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from lists.models import Item


def home_page(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        new_list_item_text = request.POST['item_text']
        Item.objects.create(text=new_list_item_text)
        return HttpResponseRedirect('/lists/')
    context = {'list_items': Item.objects.all()}
    return render(request, 'home.html', context)
