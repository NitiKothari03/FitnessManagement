from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('signup/', views.trainee_signup, name='trainee_signup'),
    path('login/', LoginView.as_view(), name='login')
]