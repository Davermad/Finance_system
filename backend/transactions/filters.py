import django_filters
from .models import Category, Transaction

class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Category
        fields = ['name']

class TransactionFilter(django_filters.FilterSet):
    created = django_filters.DateFromToRangeFilter(field_name='created')
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all())
    amount = django_filters.RangeFilter(field_name='amount')

    class Meta:
        model = Transaction
        fields = ['created', 'category', 'amount']