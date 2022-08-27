from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home_page(request: HttpRequest) -> HttpResponse:
    context = {'new_item_text': request.POST.get('item_text', '')}
    return render(request, 'home.html', context)
