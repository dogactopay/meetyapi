from .models import Balance, Transaction


def show_balance(user_id):
    resp = Balance.objects.filter(user_balance=user_id).values()

    if len(resp) > 0:
        return resp[0]["balance"]
    else:
        return 0


def new_transaction(user_id, amount, transaction_type):
    Transaction.objects.create(
        user=user_id, amount=amount, transaction_type=transaction_type)

    try:
        current_bal = Balance.objects.filter(
            user_balance=user_id).values()[0]['balance']

    except:
        current_bal = ""

    if len(str(current_bal)) > 0:
        Balance.objects.filter(user_balance=user_id).update(
            balance=float(current_bal) + float(amount))
    else:
        Balance.objects.create(user_balance=user_id, balance=float(amount))
