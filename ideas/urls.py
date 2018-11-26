from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('history/', views.get_historian, name='history'),
    path('track/<idea_id>', views.get_idea_history, name='idea_history'),
    path('logged/', views.logged, name='logged'),
    path('report/', views.report, name='report'),
    path('idea/<idea_id>/', views.idea, name='idea'),
    path('new/', views.idea_new, name='idea_new'),
    path('update/<idea_id>/', views.idea_update, name='idea_update'),
    path('txn/<txn_id>/', views.txn_details, name='txn_details'),
    # path('profile/<user_id>/', views.profile, name='profile'),
]
