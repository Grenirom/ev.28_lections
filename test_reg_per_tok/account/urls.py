from dj_rest_auth.views import LoginView
from django.urls import path

from account.views import UserRegistrationView, UserListView, UserDetailView

urlpatterns = [
    path('register/', UserRegistrationView.as_view()),
    path('login/', LoginView.as_view()),
    path('users/', UserListView.as_view()),
    path('users/<int:pk>/', UserDetailView.as_view())
]