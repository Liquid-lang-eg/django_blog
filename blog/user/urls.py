from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('sign_in/', views.sign_in_view, name='sign_in'),
    path('logout/', views.logout_view, name='logout'),
    path('sign_up/', views.sign_up_view, name='sign_up')
]