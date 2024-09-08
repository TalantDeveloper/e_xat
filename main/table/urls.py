from django.urls import path
from main.table.tableViews import *

app_name = 'table'

urlpatterns = [
    path('control-cards/', control_card_view, name='control_cards'),
    path('control-cards/<int:pk>/update/', control_card_update, name='control_cards_update'),
    path('control-cards/<int:pk>/delete/', control_card_delete, name='control_cards_delete'),

    path('groups/', groups_view, name='groups'),
    path('groups/<int:pk>/update/', groups_update, name='groups_update'),
    path('groups/<int:pk>/delete/', groups_delete, name='groups_delete'),

    path('reporters/', reporters_view, name='reporters'),
    path('reporters/<int:pk>/update/', reporters_update, name='reporters_update'),
    path('reporters/<int:pk>/delete/', reporters_delete, name='reporters_delete'),

    path('document-types/', document_types_view, name='document_types'),
    path('document-types/<int:pk>/update/', document_types_update, name='document_types_update'),
    path('document-types/<int:pk>/delete/', document_types_delete, name='document_types_delete'),

    path('author-resolutions/', author_resolutions_view, name='author_resolutions'),
    path('author-resolutions/<int:pk>/update/', author_resolutions_update, name='author_resolutions_update'),
    path('author-resolutions/<int:pk>/delete/', author_resolutions_delete, name='author_resolutions_delete'),

    path('type-solutions/', type_solutions_view, name='type_solutions'),
    path('type-solutions/<int:pk>/update/', type_solutions_update, name='type_solutions_update'),
    path('type-solutions/<int:pk>/delete/', type_solutions_delete, name='type_solutions_delete'),
]
