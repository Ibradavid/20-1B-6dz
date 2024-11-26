from django.urls import path
from apps.users.views import RegisterView, UserDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('me/', UserDetailView.as_view(), name='user-detail'),  # Получить или обновить текущего пользователя
]
