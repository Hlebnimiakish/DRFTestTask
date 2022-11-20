import django_filters
from potential_app.models import UserTransactions


class UserTransactionsFilterOrder(django_filters.FilterSet):
    tr_date = django_filters.DateTimeFilter(field_name='tr_datetime', lookup_expr='__date')
    tr_time = django_filters.DateTimeFilter(field_name='tr_datetime', lookup_expr='__time')

    order_by_field = 'order'
    order = django_filters.OrderingFilter(fields=(
        ('tr_datetime', "tr_datetime"),
        ('tr_datetime__date', 'tr_date'),
        ('tr_datetime__time', 'tr_time'),
        ('tr_value', 'tr_value'),
    ))

    class Meta:
        model = UserTransactions
        fields = ['tr_value']