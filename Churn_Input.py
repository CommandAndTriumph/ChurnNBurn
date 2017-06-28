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
            # json.dump({'Amount': amount, 'Balance Amount': balance_amount, 'Minimum Transactions': minimum_transactions, 'Issue Date': issue_date.isoformat(), 'No Action Expiration Timedelta': unacted_expiration_timedelta.days, 'Action Timedelta': action_timedelta.days, 'Account Active Age': account_active_age, 'Account Dormant Age': account_dormant_age}, fp, indent = 4)


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

        with open(f'{offer_name}.json', 'w') as fp:
            json.dump({'Amount': amount, 'Deposit Amount': deposit_amount, 'Monthly Deposits': num_monthly_deposits, 'Max Withdrawals': num_permissible_withdrawals, 'Minimum Account Balance': min_account_balance, 'Issue Date': issue_date.isoformat(), 'No Action Expiration Date': unacted_expiration_timedelta.days, 'Action Timedelta': action_timedelta.days, 'Account Active Age': account_active_age, 'Account Dormant Age': account_dormant_age}, fp, indent = 4)

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
        additional_accounts_required = bool(input('Are additional accounts required? (Enter True or False) '))
        issue_date = datetime.datetime.strptime(input('Offer Issue Date (input as MMDDYYYY): '), '%m%d%Y')
        unacted_expiration_timedelta = datetime.timedelta(days=float(input('The number of days you have until the offer expires: ')))
        action_timedelta = datetime.timedelta(days=float(input('How many days do you have after registering for the offer to take the first step? ')))
        account_active_age = int(input('How many months do you need to satisfy the above criteria? '))
        account_dormant_age = int(input('How many months does the account need to remain dormant after activity on it has ceased? '))

        with open(f'{offer_name}.json', 'w') as fp:
            json.dump({'Amount': amount, 'First Deposit Amount': initial_deposit_amount, 'Minimum Balance': account_min_bal, 'Min Monthly Deposits': num_monthly_deposits, 'Min Monthly Withdrawals': num_monthly_withdrawls, 'Minimum Monthly Deposit Amount': min_monthly_deposit_amount, 'Minimum Monthly Withdrawal Amount': min_monthly_withdrawal_amount, 'Additional Accounts Required (Boolean)': additional_accounts_required, 'Issue Date': issue_date.isoformat(), 'No Action Expiration Date': unacted_expiration_timedelta.days, 'Action Timedelta': action_timedelta.days, 'Account Active Age': account_active_age, 'Account Dormant Age': account_dormant_age}, fp, indent = 4)

        pass

CC_Input()
