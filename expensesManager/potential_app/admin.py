from django.contrib import admin
from .models import TransactionsCategories, UserTransactions

admin.site.register(TransactionsCategories)

admin.site.register(UserTransactions)
