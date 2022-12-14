from django.conf.urls import url

from lists.views import view_list, new_list, add_item

urlpatterns = [
    url(r'(\d+)/$', view_list, name='view_list'),
    url(r'new/$', new_list, name='new_list'),
    url(r'(\d+)/add-item/$', add_item, name='add_item'),
]
