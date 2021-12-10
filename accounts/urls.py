from django.urls import path
from . import views
# from django.contrib.auth.views import LoginView
from django.views.generic.base import RedirectView

app_name= 'accounts'

urlpatterns = [
    path('', views.mylogin, name='login'),
    path('login/', views.mylogin, name = 'login'),
    path('signup/', views.signup, name = 'signup'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
    path('profile/<slug:userURL>', views.profile, name='profile'),
]
