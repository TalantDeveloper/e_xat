from django.urls import path

from main.views.centerViews import centers_view
from main.views.userViews import login_view, logout_view
from main.views.views import welcome, today_view, finish_view, manager_out_view, create_manager_view, view_manager

app_name = 'main'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),


    
    path('', welcome, name='welcome'),
    path('today/', today_view, name='today'),
    path('finish/', finish_view, name='finish'),
    path('timeout/', manager_out_view, name='timeout'),

    path('manager-add/', create_manager_view, name='manager-add'),
    path('manager/<int:manager_id>/update/', view_manager, name='manager-update'),


    path('centers/', centers_view, name='centers'),

]
