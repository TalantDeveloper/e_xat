from django.urls import path
from main.table.tableViews import *

app_name = 'table'

urlpatterns = [
    path('controlcards/', control_card_view, name='control_cards'),
    path('controlcards/<int:pk>/update/', control_card_update, name='control_cards_update'),
    path('controlcards/<int:pk>/delete/', control_card_delete, name='control_cards_delete'),

    path('groups/', groups_view, name='groups'),
    path('groups/<int:pk>/update/', groups_update, name='groups_update'),
    path('groups/<int:pk>/delete/', groups_delete, name='groups_delete'),

    path('reporters/', reporters_view, name='reporters'),
    path('reporters/<int:pk>/update/', reporters_update, name='reporters_update'),
    path('reporters/<int:pk>/delete/', reporters_delete, name='reporters_delete'),

    path('documenttypes/', document_types_view, name='document_types'),
    path('documenttypes/<int:pk>/update/', document_types_update, name='document_types_update'),
    path('documenttypes/<int:pk>/delete/', document_types_delete, name='document_types_delete'),

    path('author_resolutions/', author_resolutions_view, name='author_resolutions'),
    path('author_resolutions/<int:pk>/update/', author_resolutions_update, name='author_resolutions_update'),
    path('author_resolutions/<int:pk>/delete/', author_resolutions_delete, name='author_resolutions_delete'),



]
