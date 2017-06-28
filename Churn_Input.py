import json, datetime, jsonpickle
from Churn_Models import*

class CC_Input:
    def __init__(self):
        offer_name = input('Offer Name: ')
        amount = float(input('Bonus Amount: '))
        balance_amount = float(input('Monthly Balance to be Paid Off each Month: '))
        minimum_transactions = int(input('Number of Transactions which must be made each month (enter 0 if None/Not Applicable): '))
        issue_date = datetime.datetime.strptime(input('Offer Issue Date (input as MMDDYYYY): '), '%m%d%Y')
        unacted_expiration_timedelta = datetime.timedelta(days = float(input('The number of days you have until the offer expires: ')))
        action_timedelta = datetime.timedelta(days = float(input('How many days do you have after registering for the offer to take the first step? ')))
        account_active_age = int(input('How many months do you need to accrue a balance and pay it off? '))
        account_dormant_age = int(input('How many months does the account need to remain dormant after activity on it has ceased? '))
        cc_offer = CC_Offer_Terms(offer_name, amount, balance_amount, minimum_transactions, issue_date, unacted_expiration_timedelta, action_timedelta, account_active_age, account_dormant_age)
        with open(f'{offer_name}.json', 'w') as fp:
            fp.write(jsonpickle.dumps(cc_offer))

class SA_Input:
    def __init__(self):
        offer_name = input('Offer Name: ')
        amount = float(input('Bonus Amount: '))
        deposit_amount = float(input('Initial Deposit Required: '))
        num_monthly_deposits = int(input('Minimum Deposits per Month: '))
        num_permissible_withdrawals = int(input('Maximum Number of Withdrawals per Month: '))
        min_account_balance = float(input('Minimum Balance which Must be Maintained Each Month: '))
        issue_date = datetime.datetime.strptime(input('Offer Issue Date (input as MMDDYYYY): '), '%m%d%Y')
        unacted_expiration_timedelta = datetime.timedelta(days=float(input('The number of days you have until the offer expires: ')))
        action_timedelta = datetime.timedelta(days=float(input('How many days do you have after registering for the offer to take the first step? ')))
        account_active_age = int(input('How many months do you need to satisfy the above criteria? '))
        account_dormant_age = int(input('How many months does the account need to remain dormant after activity on it has ceased? '))
        sa_offer = SA_Offer_Terms(offer_name, amount, deposit_amount, num_monthly_deposits, num_permissible_withdrawals, min_account_balance, issue_date, unacted_expiration_timedelta, action_timedelta, account_active_age, account_dormant_age)
        with open(f'{offer_name}.json', 'w') as fp:
            fp.write(jsonpickle.dumps(sa_offer))

class CA_Input:
    def __init__(self):
        offer_name = input('Offer Name: ')
        amount = float(input('Bonus Amount: '))
        initial_deposit_amount = float(input('Intial Deposit Required: '))
        account_min_bal = float(input('Minimum Balance which must be maintained in the account: '))
        num_monthly_deposits = int(input('How many deposits need to made each month? '))
        num_monthly_withdrawls = int(input('How many withdrawals need to be made each month? '))
        min_monthly_deposit_amount = float(input('How much, in total, must be deposited each month? '))
        min_monthly_withdrawal_amount = float(input('How much, in total, must be withdrawn each month? '))
        additional_accounts_required = self.boolean_helper(input('Are additional accounts required? (Enter True or False) '))
        issue_date = datetime.datetime.strptime(input('Offer Issue Date (input as MMDDYYYY): '), '%m%d%Y')
        unacted_expiration_timedelta = datetime.timedelta(days=float(input('The number of days you have until the offer expires: ')))
        action_timedelta = datetime.timedelta(days=float(input('How many days do you have after registering for the offer to take the first step? ')))
        account_active_age = int(input('How many months do you need to satisfy the above criteria? '))
        account_dormant_age = int(input('How many months does the account need to remain dormant after activity on it has ceased? '))
        ca_offer = CA_Offer_Terms(offer_name, amount, initial_deposit_amount, account_min_bal, num_monthly_deposits, num_monthly_withdrawls, min_monthly_deposit_amount, min_monthly_withdrawal_amount, additional_accounts_required, issue_date, unacted_expiration_timedelta, action_timedelta, account_active_age, account_dormant_age)
        with open(f'{offer_name}.json', 'w') as fp:
            fp.write(jsonpickle.dumps(ca_offer))

    @staticmethod
    def boolean_helper(b):
        if b == 'False':
            return False
        elif b == 'True':
            return True
        elif b == 'true':
            return True
        elif b == 'false':
            return False
        raise ValueError("Input must be True or False")


churn_start = str.lower(input('Is the offer for a Checking Account, Savings Account, or Credit Card? (Enter CA, SA, or CC): '))
if churn_start == 'cc':
    CC_Input()
elif churn_start == 'sa':
    SA_Input()
elif churn_start == 'ca':
    CA_Input()
else:
    raise ValueError('Input must be CA, SA, or CC')


