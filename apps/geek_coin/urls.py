from django.urls import path
from apps.geek_coin.views import TransferCoinsView, BurnCoinsView, TransactionHistoryView

urlpatterns = [
    path('transfer/', TransferCoinsView.as_view(), name='transfer-coins'),
    path('burn/', BurnCoinsView.as_view(), name='burn-coins'),
    path('history/', TransactionHistoryView.as_view(), name='transaction-history'),
]
