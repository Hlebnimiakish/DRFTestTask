from potential_app.models import UserBalance, UserTransactions, TransactionsCategories
from django.shortcuts import get_object_or_404


def balance_getter(api_func):
    def wrapper(*args, **kwargs):
        try:
            user_balance = UserBalance.objects.get(user_id=args[1].data['tr_user'])
            return api_func(*args, user_balance, **kwargs)
        except UserBalance.DoesNotExist:
            user_balance = UserBalance.objects.create(user_id=args[1].data['tr_user'])
            return api_func(*args, user_balance, **kwargs)
    return wrapper


def transaction_getter_by_id(api_func):
    def wrapper(*args, **kwargs):
        tr_set = UserTransactions.objects.all()
        transaction = get_object_or_404(tr_set, id=kwargs['id'])
        return api_func(*args, transaction=transaction, **kwargs)
    return wrapper


def category_user_getter_by_id(api_func):
    def wrapper(*args, **kwargs):
        user = args[1].user
        usr_categories_set = TransactionsCategories.objects.filter(tr_ctg_user=user)
        usr_category = get_object_or_404(usr_categories_set, id=kwargs['id'])
        return api_func(*args, usr_category=usr_category, user=user, **kwargs)
    return wrapper



