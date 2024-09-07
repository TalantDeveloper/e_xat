from django.urls import path

from main.views.centerViews import centers_view, center_edit_view, delete_center
from main.views.userViews import login_view, logout_view, view_users, create_user_view, edit_user_view, delete_user_view
from main.views.views import welcome, today_view, finish_view, manager_out_view, create_manager_view, view_manager

app_name = 'main'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('users/', view_users, name='users'),
    path('user/', create_user_view, name='add-user'),
    path('user/<int:user_id>/update', edit_user_view, name='update-user'),
    path('user/<int:user_id>/delete', delete_user_view, name='delete-user'),

    
    path('', welcome, name='welcome'),
    path('today/', today_view, name='today'),
    path('finish/', finish_view, name='finish'),
    path('timeout/', manager_out_view, name='timeout'),

    path('manager-add/', create_manager_view, name='manager-add'),
    path('manager/<int:manager_id>/update/', view_manager, name='manager-update'),


    path('centers/', centers_view, name='centers'),
    path('centers/<int:center_id>/update', center_edit_view, name='center-update'),
    path('centers/<int:center_id>/delete/', delete_center, name='center-delete'),

]
