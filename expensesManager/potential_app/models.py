from django.db import models
from django.contrib.auth.models import User


class TransactionsCategories(models.Model):
    tr_ctg_name = models.CharField(max_length=100)
    tr_ctg_user = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.tr_ctg_name


class UserTransactions(models.Model):
    tr_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False)
    tr_value = models.FloatField(blank=False)
    tr_datetime = models.DateTimeField(auto_now_add=True)
    tr_category = models.ForeignKey(TransactionsCategories, models.SET_NULL, null=True, blank=True)
    tr_organisation = models.CharField(max_length=100, blank=False)
    tr_description = models.TextField(blank=True)

    def __str__(self):
        return self.tr_description






