from django.conf.urls import url
from . import views

app_name='Game'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    #url(r'^list/$',views.list, name='list'),
    #url(r'^group/$',views.group, name='group'),
    url(r'^sportform/$',views.sportform, name='sportform'),#done
    url(r'^creategroup/$',views.creategroup, name='creategroup'),
    url(r'^update/$',views.update, name='update'),#done
]