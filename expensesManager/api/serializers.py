from rest_framework import serializers
from potential_app.models import TransactionsCategories, UserTransactions, User


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UserTransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTransactions
        fields = '__all__'


class TransactionsCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionsCategories
        fields = '__all__'



