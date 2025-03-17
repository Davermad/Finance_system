from django.urls import path
from .views import CategoryListCreate, CategoryDetail, TransactionListCreate, TransactionDetail, UserListCreate, UserDetail
from .export_csv import export_transactions_csv
from .export_pdf import export_transactions_pdf

urlpatterns = [
    path('categories/', CategoryListCreate.as_view(), name='categories'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category'),
    path('transactions/', TransactionListCreate.as_view(), name='transactions'),
    path('transactions/<int:pk>/', TransactionDetail.as_view(), name='transaction'),
    path('users', UserListCreate.as_view(), name='users'),
    path('users/<int:pk>', UserDetail.as_view(), name='user'),
    path('export/csv/', export_transactions_csv, name='export-transactions-csv'),
    path('export/pdf/', export_transactions_pdf, name='export-transactions-pdf'),

]