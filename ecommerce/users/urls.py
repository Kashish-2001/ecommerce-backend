from django.urls import path
from .views import CustomUserView

urlpatterns = [
    path('user-detail/', CustomUserView.as_view(), name='user-detail')
]
