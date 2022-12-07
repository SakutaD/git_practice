from .views import RegisterUserView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('register/', RegisterUserView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('toke/refresh/', TokenRefreshView.as_view())
]