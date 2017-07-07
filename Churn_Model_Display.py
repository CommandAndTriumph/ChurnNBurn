import os
from Churn_Models import*
folder = 'JSON'

class CC_Read:
    @staticmethod
    def cc_scan():
        cc_list = [x for x in os.listdir(folder) if x.startswith('CC_') == True]
        print('Credit Card Offers: \n')
        for i in cc_list:
            jsonread = Offer.read_from_json_file(f'{folder}/{i}')
            print(jsonread.offer_name)
            print(f'Reward Amount: ${jsonread.amount}')
            print(f'Required Monthly Balance: ${jsonread.balance_amount}')
            print(f'Minimum Monthly Transactions: {jsonread.minimum_transactions}')
            print(f'Offer Issue Date: {jsonread.issue_date}')
            print(f'Days to act on offer from issue date: {jsonread.unacted_expiration_timedelta}')
            print(f'Days once action is taken to complete first step: {jsonread.action_timedelta}')
            print(f'Account Active Age: {jsonread.account_active_age}')
            print(f'Account Dormant Age: {jsonread.account_dormant_age}')
            print('\n')


class SA_Read:
    @staticmethod
    def sa_scan():
        sa_list = [x for x in os.listdir(folder) if x.startswith('SA_') == True]
        print('Savings Accout Offers: \n')
        for i in sa_list:
            jsonread = Offer.read_from_json_file(f'{folder}/{i}')
            print(jsonread.offer_name)
            print(f'Reward Amount: ${jsonread.amount}')
            print(f'Initial Deposit Amount: ${jsonread.deposit_amount}')
            print(f'Minimum Monthly Deposits: {jsonread.num_monthly_deposits}')
            print(f'Maximum Monthly Withdrawals: {jsonread.num_permissible_withdrawals}')
            print(f'Minimum Account Balance: ${jsonread.min_account_balance}')
            print(f'Offer Issue Date: {jsonread.issue_date}')
            print(f'Days to act on offer from issue date: {jsonread.unacted_expiration_timedelta}')
            print(f'Days once action is taken to complete first step: {jsonread.action_timedelta}')
            print(f'Account Active Age: {jsonread.account_active_age}')
            print(f'Account Dormant Age: {jsonread.account_dormant_age}')
            print('\n')

class CA_Read:
    @staticmethod
    def ca_scan():
        ca_list = [x for x in os.listdir(folder) if x.startswith('CA_') == True]
        print('Checking Account Offers: \n')
        for i in ca_list:
            jsonread = Offer.read_from_json_file(f'{folder}/{i}')
            print(jsonread.offer_name)
            print(f'Reward Amount: ${jsonread.amount}')
            print(f'Initial Deposit Amount: ${jsonread.initial_deposit_amount}')
            print(f'Minimum Account Balance: ${jsonread.account_min_bal}')
            print(f'Minimum Monthly Deposits: {jsonread.num_monthly_deposits}')
            print(f'Minimum Monthly Withdrawals: {jsonread.num_monthly_withdrawals}')
            print(f'Minimum Monthly Deposit Amount: ${jsonread.min_monthly_deposit_amount}')
            print(f'Minimum Monthly Withdrawal Amount: ${jsonread.min_monthly_withdrawal_amount}')
            print(f'Are Additional Accounts Required? {jsonread.additional_accounts_required}')
            print(f'Offer Issue Date: {jsonread.issue_date}')
            print(f'Days to act on offer from issue date: {jsonread.unacted_expiration_timedelta}')
            print(f'Days once action is taken to complete first step: {jsonread.action_timedelta}')
            print(f'Account Active Age: {jsonread.account_active_age}')
            print(f'Account Dormant Age: {jsonread.account_dormant_age}')
            print('\n')

CC_Read.cc_scan()
# SA_Read.sa_scan()
# CA_Read.ca_scan()