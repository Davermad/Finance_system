import csv
from django.http import HttpResponse
from .models import Transaction

def export_transactions_csv(request):
    """Экспорт транзакций в CSV"""
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="transactions.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'User', 'Category', 'Amount', 'Date'])

    transactions = Transaction.objects.filter(user=request.user)
    for transaction in transactions:
        writer.writerow([transaction.id, transaction.user, transaction.category.name, transaction.amount, transaction.created])

    return response
