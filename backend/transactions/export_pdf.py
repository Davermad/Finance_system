from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from .models import Transaction

def export_transactions_pdf(request):
    """Экспорт транзакций в PDF"""
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="transactions.pdf"'

    pdf = canvas.Canvas(response, pagesize=letter)
    pdf.setTitle("Transactions Report")

    pdf.drawString(100, 750, "Список транзакций")
    pdf.drawString(100, 730, "ID | Категория | Сумма | Дата")

    transactions = Transaction.objects.filter(user=request.user)
    y_position = 710
    for transaction in transactions:
        pdf.drawString(100, y_position, f"{transaction.id} | {transaction.user} | {transaction.category.name} | {transaction.amount} | {transaction.created}")
        y_position -= 20  # Смещаем вниз

    pdf.save()
    return response
