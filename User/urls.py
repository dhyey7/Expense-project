from django.urls import path
from User.views import *

urlpatterns = [
    path('dashboard/', dashboard, name = 'dashboard'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path("logout/", logout_request, name="logout"),
]
