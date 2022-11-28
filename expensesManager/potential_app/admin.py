from django.contrib import admin
from .models import TransactionsCategories, UserTransactions, UserBalance


@admin.register(TransactionsCategories)
class AdminTransactionCategories(admin.ModelAdmin):
    list_display = ('tr_ctg_name', )
    list_display_links = ('tr_ctg_name', )


@admin.register(UserTransactions)
class AdminUserTransactions(admin.ModelAdmin):
    list_display = ('tr_user', 'tr_value', 'tr_datetime', 'tr_category', )
    list_display_links = ('tr_user', 'tr_category', )


@admin.register(UserBalance)
class AdminUserBalance(admin.ModelAdmin):
    list_display = ('user_id', 'balance_value', )
    list_display_links = ('user_id', )
