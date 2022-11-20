from potential_app.models import UserTransactions
from django.contrib.auth import get_user_model
from django.db.models import Sum, Count
import datetime
from django.core.mail import send_mail



def collected_stats_msg(user_id):

    '''
    :param user_id:
    :return: сформированное сообщение с созданной статистикой пользователя
    '''

    usr_trs = UserTransactions.objects.filter(tr_user=user_id)
    usr_trs_yday = usr_trs.filter(tr_datetime__date=(datetime.date.today()-datetime.timedelta(days=1)))
    usr_trs_number = usr_trs_yday.aggregate(Count('id'))['id__count']
    usr_day_expenses = usr_trs_yday.filter(tr_value__lte=0).aggregate(Sum('tr_value'))['tr_value__sum']
    usr_day_income = usr_trs_yday.filter(tr_value__gt=0).aggregate(Sum('tr_value'))['tr_value__sum']
    return f'''\nДобрый день, направляем вам статистику за предыдущий день.\n 
    Количество транзакций: {usr_trs_number}.\n 
    Расходы за день: {usr_day_expenses}.\n
    Поступления за день: {usr_day_income}.\n
    С Уважением, Ваш Менеджер расходов'''


def sender():
    users = get_user_model().objects.all()
    for user in users:
        message = str(collected_stats_msg(user.id))
        send_mail(
            'Ваша статистика за предыдущий день',
            str(message),
            'ExpensesManager@mail.com',
            [f'{user.email}'],
            fail_silently=False,
        )


