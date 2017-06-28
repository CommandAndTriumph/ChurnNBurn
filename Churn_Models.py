import datetime

class CC_Offer_Terms:
    def __init__(self, offer_name, amount, balance_amount, minimum_transactions, issue_date, unacted_expiration_timedelta, action_timedelta, account_active_age, account_dormant_age):

        '''  
        :ivar offer_name:  Name of the offer.
        :ivar amount: Cash amount of the offer (float)
        :ivar balance_amount: Monthly balance which must be accrued and paid off each month.  (float)
        :ivar mininium_transactions: Minimum number of transactions required to build balance_amount.  (int)
        :ivar issue_date: Issue date of the offer (datetime)
        :ivar unacted_expiration_timedelta: The amount of time you have to act on the offer.  (timedelta)
        :ivar action_timedelta: The amount of time once you register for the offer to complete the first step.  (timedelta)
        :ivar account_active_age: How many months you need to rack up a balance and pay it off.  (int)
        :ivar account_dormant_age: How long after ceasing activity on the account, do you need to maintain it for (when can you close it?) (int)
        '''

        self.offer_name = offer_name
        self.amount = amount
        self.balance_amount = balance_amount
        self.minimum_transactions = minimum_transactions
        self.issue_date = issue_date
        self.unacted_expiration_timedelta = unacted_expiration_timedelta
        self.action_timedelta = action_timedelta
        self.account_active_age = account_active_age
        self.account_dormant_age = account_dormant_age

        # offer_name = input('Offer Name: ')
        # amount = float(input('Bonus Amount: '))
        # balance_amount = float(input('Monthly Balance to be Paid Off each Month: '))
        # minimum_transactions = int(input('Number of Transactions which must be made each month (enter 0 if None/Not Applicable): '))
        # issue_date = datetime.datetime.strptime(input('Offer Issue Date (input as MMDDYYYY): '), '%m%d%Y')
        # unacted_expiration_timedelta = datetime.timedelta(days = float(input('The number of days you have until the offer expires: ')))
        # action_timedelta = datetime.timedelta(days = float(input('How many days do you have after registering for the offer to take the first step? ')))
        # account_active_age = int(input('How many months do you need to accrue a balance and pay it off? '))
        # account_dormant_age = int(input('How many months does the account need to remain dormant after activity on it has ceased? '))

        # with open(f'{offer_name}.json', 'w') as fp:
            # json.dump({'Amount': amount, 'Balance Amount': balance_amount, 'Minimum Transactions': minimum_transactions, 'Issue Date': issue_date.isoformat(), 'No Action Expiration Date': unacted_expiration_timedelta.days, 'Action Timedelta': action_timedelta.days, 'Account Active Age': account_active_age, 'Account Dormant Age': account_dormant_age}, fp, indent = 4)


class SA_Offer_Terms:
    def __init__(self, offer_name, amount, deposit_amount, num_monthly_deposits, num_permissible_withdrawls, min_account_balance, issue_date, unacted_expiration_timedelta, action_timedelta, account_active_age, account_dormant_age):
        '''
        :ivar offer_name:  The name of the offer
        :ivar amount:  Cash value of the offer (float) 
        :ivar deposit_amount: Initial deposit required (float)
        :ivar num_monthly_deposits: How many times per month a deposit to the account must be made (int)
        :ivar num_permissible_withdrawls: How many withdrawals, in the span of one month, can be made from the account (int)
        :ivar min_account_balance: The minimum balance the account must have to still qualify for the offer (float)
        :ivar issue_date:  The date the offer is issued (datetime)
        :ivar unacted_expiration_timedelta: The amount of time you have to act on the offer (timedelta)
        :ivar action_timedelta: How long you have after registering for the offer to complete the first step (timedelta)
        :ivar account_active_age: How long you must keep doing stuff to the account per the above terms (days, int)
        :ivar account_dormant_age: How long you must keep the account in a dormant state (days, int)
        '''
        self.offer_name = offer_name
        self.amount = amount
        self.deposit_amount = deposit_amount
        self.num_monthly_deposits = num_monthly_deposits
        self.num_permissible_withdrawals = num_permissible_withdrawls
        self.min_account_balance = min_account_balance
        self.issue_date = issue_date
        self.unacted_expiration_timedelta = unacted_expiration_timedelta
        self.action_timedelta = action_timedelta
        self.account_active_age = account_active_age
        self.account_dormant_age = account_dormant_age


class CA_Offer_Terms:
    def __init__(self, offer_name, amount, initial_deposit_amount, account_min_bal, num_monthly_deposits, num_monthly_withdrawals, min_monthly_deposit_amount, min_monthly_withdrawal_amount, additional_accounts_required, issue_date, unacted_expiration_timedelta, action_timedelta, account_active_age, account_dormant_age):
        '''
        :ivar offer_name:  The name of the offer
        :ivar amount: Cash value of the offer (float)
        :ivar initial_deposit_amount: Initial deposit required (float)
        :ivar account_min_bal: Minimum balance the account must have at all times (float)
        :ivar num_monthly_deposits: How many deposits must be made to the accout each month (int)
        :ivar num_monthly_withdrawals: How many withdrawals must be made to the account each month (int)
        :ivar min_monthly_deposit_amount: How much each month's deposits must be (float)
        :ivar min_monthly_withdrawal_amount: How much each month's withdrawals must be (float)
        :ivar additional_accounts_required: Are additional accounts required?  (boolean)
        :ivar issue_date: Date the offer was issued (datetime)
        :ivar unacted_expiration_timedelta: How many days the offer is valid for (timedelta)
        :ivar action_timedelta: How long you have to complete the first step in the offer after registering for it (timedelta)
        :ivar account_active_age:  How long you must keep doing stuff to the account per the above terms(days, int)
        :ivar account_dormant_age: How long the account must be kept in a dormant state (days, int)
        '''
        self.offer_name = offer_name
        self.amount = amount
        self.initial_deposit_amount = initial_deposit_amount
        self.account_min_bal = account_min_bal
        self.num_monthly_deposits = num_monthly_deposits
        self.num_monthly_withdrawals = num_monthly_withdrawals
        self.min_monthly_deposit_amount = min_monthly_deposit_amount
        self.min_monthly_withdrawal_amount = min_monthly_withdrawal_amount
        self.additonal_accounts_required = additional_accounts_required
        self.issue_date = issue_date
        self.unacted_expiration_timedelta = unacted_expiration_timedelta
        self.action_timedelta = action_timedelta
        self.account_active_age = account_active_age
        self.account_dormant_age = account_dormant_age
        



chase1 = CC_Offer_Terms('Chase Sapphire', 200, 1000, 10, datetime.datetime(2017, 10, 23), datetime.timedelta(days = 30), datetime.timedelta(days = 60), 180, 360)

print(f'The offer amount is ${chase1.amount}.')
print(f'The offer is good for {chase1.action_timedelta.days} days after you choose to act upon it')