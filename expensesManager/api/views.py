from django_filters import rest_framework
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from api.transactions_filter_order import UserTransactionsFilterOrder
from django.shortcuts import get_object_or_404
from rest_framework import status, generics, viewsets
from django.db.models import Sum
from potential_app.models import TransactionsCategories, UserTransactions
from .serializers import CreateUserSerializer, UserTransactionsSerializer, TransactionsCategoriesSerializer


class GlobalTransactionsCRUDAPIView(viewsets.ViewSet):
    permission_classes = [IsAdminUser]
    """
        superuser = username: admin, password: 12345
    """

    def list(self, request):
        tr_set = UserTransactions.objects.all()
        serialized_tr = UserTransactionsSerializer(tr_set, many=True)
        return Response(serialized_tr.data)

    def retrive(self, request, id=None):
        tr_set = UserTransactions.objects.all()
        transaction = get_object_or_404(tr_set, id=id)
        serialized_tr = UserTransactionsSerializer(transaction)
        return Response(serialized_tr.data)

    def create(self, request):
        serialized_tr = UserTransactionsSerializer(data=request.data)
        if serialized_tr.is_valid():
            serialized_tr.save()
            return Response(serialized_tr.data)
        else:
            return Response(serialized_tr.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, id=None):
        tr_set = UserTransactions.objects.all()
        transaction = get_object_or_404(tr_set, id=id)
        upd_serialized_tr = UserTransactionsSerializer(data=request.data, instance=transaction)
        if transaction and upd_serialized_tr.is_valid():
            upd_serialized_tr.save()
            return Response(upd_serialized_tr.data)
        else:
            return Response(upd_serialized_tr.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, id=None):
        tr_set = UserTransactions.objects.all()
        transaction = get_object_or_404(tr_set, id=id)
        transaction.delete()
        return Response(status=status.HTTP_200_OK)


class UserTransactionsAPIView(generics.ListAPIView):
    queryset = UserTransactions.objects.all()
    serializer_class = UserTransactionsSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (rest_framework.DjangoFilterBackend, )
    filterset_class = UserTransactionsFilterOrder


class CreateUserAPIView(APIView):

    def post(self, request):
        serialized_cr_user = CreateUserSerializer(data=request.data)
        if serialized_cr_user.is_valid():
            sv = serialized_cr_user.save()
            for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
                ct = TransactionsCategories.objects.get(id=i)
                ct.tr_ctg_user.add(sv)
            return Response(serialized_cr_user.data)
        else:
            return Response(serialized_cr_user.errors, status=status.HTTP_400_BAD_REQUEST)


class UserCategoriesAPIView(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        user = request.user
        usr_categories_set = TransactionsCategories.objects.filter(tr_ctg_user=user)
        serialized_usr_ctg = TransactionsCategoriesSerializer(usr_categories_set, many=True)
        return Response(serialized_usr_ctg.data)

    def retrive(self, request, id=None):
        user = request.user
        usr_categories_set = TransactionsCategories.objects.filter(tr_ctg_user=user)
        usr_category = get_object_or_404(usr_categories_set, id=id)
        serialized_usr_ctg = TransactionsCategoriesSerializer(usr_category)
        return Response(serialized_usr_ctg.data)

    def create(self, request):
        user = request.user
        serialized_ctg = TransactionsCategoriesSerializer(data=request.data)
        if serialized_ctg.is_valid():
            sv = serialized_ctg.save()
            sv.tr_ctg_user.add(user)
            return Response(serialized_ctg.data)
        else:
            return Response(serialized_ctg.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, id=None):
        user = request.user
        usr_categories_set = TransactionsCategories.objects.filter(tr_ctg_user=user)
        usr_category = get_object_or_404(usr_categories_set, id=id)
        tr_to_update = UserTransactions.objects.filter(tr_user=user, tr_category=usr_category)
        serialized_upd_ctg = TransactionsCategoriesSerializer(data=request.data)
        if usr_category.id <= 11:
            if serialized_upd_ctg.is_valid():
                usr_category.tr_ctg_user.remove(user)
                sv = serialized_upd_ctg.save()
                sv.tr_ctg_user.add(user)
                tr_to_update.update(tr_category=sv)
                return Response(serialized_upd_ctg.data)
            else:
                return Response(serialized_upd_ctg.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serialized_upd_ctg = TransactionsCategoriesSerializer(usr_category, data=request.data)
            if serialized_upd_ctg.is_valid():
                serialized_upd_ctg.save()
                return Response(serialized_upd_ctg.data)

    def destroy(self, request, id=None):
        user = request.user
        usr_categories_set = TransactionsCategories.objects.filter(tr_ctg_user=user)
        usr_category = get_object_or_404(usr_categories_set, id=id)
        if usr_category.id <= 11:
            usr_category.tr_ctg_user.remove(user)
            return Response(status=status.HTTP_200_OK)
        else:
            usr_category.delete()
            return Response(status=status.HTTP_200_OK)


class UserBalance(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        user_transactions = UserTransactions.objects.filter(tr_user=user.id)
        balance = user_transactions.aggregate(Sum('tr_value'))
        return Response(data={"user": request.user.username, "user_balance": round(balance['tr_value__sum'], 2)})



