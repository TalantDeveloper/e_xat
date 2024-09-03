from django.urls import path

from main.views.userViews import login_view, logout_view
from main.views.views import welcome

app_name = 'main'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    
    path('', welcome, name='welcome'),


]
