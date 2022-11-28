from django.urls import path
from rest_framework.authtoken import views

from .views import GlobalTransactionsCRUDAPIView, CreateUserAPIView, UserCategoriesAPIView, UserTransactionsAPIView, UserBalanceAPIView

urlpatterns = [
    path('transactions/', GlobalTransactionsCRUDAPIView.as_view({'get': 'list'})),
    path('transaction/add/', GlobalTransactionsCRUDAPIView.as_view({'post': 'create'})),
    path('transaction/<int:id>/', GlobalTransactionsCRUDAPIView.as_view({'get': 'retrive'})),
    path('transaction/<int:id>/change/', GlobalTransactionsCRUDAPIView.as_view({'get': 'retrive', 'put': 'update'})),
    path('transaction/<int:id>/delete/', GlobalTransactionsCRUDAPIView.as_view({'get': 'retrive', 'delete': 'destroy'})),
    path('user/add/', CreateUserAPIView.as_view()),
    path('user/auth/', views.obtain_auth_token),
    path('user_transactions/', UserTransactionsAPIView.as_view()),
    path('user_categories/', UserCategoriesAPIView.as_view({'get': 'list'})),
    path('user_category/<int:id>/', UserCategoriesAPIView.as_view({'get': 'retrive'})),
    path('user_category/add/', UserCategoriesAPIView.as_view({'post': 'create'})),
    path('user_category/<int:id>/change/', UserCategoriesAPIView.as_view({'get': 'retrive', 'put': 'update'})),
    path('user_category/<int:id>/delete/', UserCategoriesAPIView.as_view({'get': 'retrive', 'delete': 'destroy'})),
    path('user_balance', UserBalanceAPIView.as_view()),

]