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
            print('{')
            print(f'"offer_name": "{jsonread.offer_name}",')
            print(f'"amount": {jsonread.amount},')
            print(f'"balance_amount": {jsonread.balance_amount}')
            print(f'"minimum_transactions": {jsonread.minimum_transactions},')
            print(f'"issue_date": "{jsonread.issue_date}",')
            print(f'"unacted_expiration_timedelta": "{jsonread.unacted_expiration_timedelta}",')
            print(f'"action_timedelta": "{jsonread.action_timedelta}",')
            print(f'"account_active_age": {jsonread.account_active_age},')
            print(f'"account_dormant_age": {jsonread.account_dormant_age}')
            print('}')
            print('\n')


class SA_Read:
    @staticmethod
    def sa_scan():
        sa_list = [x for x in os.listdir(folder) if x.startswith('SA_') == True]
        print('Savings Accout Offers: \n')
        for i in sa_list:
            jsonread = Offer.read_from_json_file(f'{folder}/{i}')

            print('{')
            print(f'"offer_name": "{jsonread.offer_name}",')
            print(f'"amount": {jsonread.amount}'',')
            print(f'"deposit_amount": {jsonread.deposit_amount},')
            print(f'"num_monthly_deposits": {jsonread.num_monthly_deposits},')
            print(f'"num_permissible_withdrawals": {jsonread.num_permissible_withdrawals},')
            print(f'"min_account_balance": {jsonread.min_account_balance},')
            print(f'"issue_date": "{jsonread.issue_date}",')
            print(f'"unacted_expiration_timedelta": "{jsonread.unacted_expiration_timedelta}",')
            print(f'"action_timedelta": "{jsonread.action_timedelta}",')
            print(f'"account_active_age": {jsonread.account_active_age},')
            print(f'"account_dormant_age": {jsonread.account_dormant_age}')
            print('}')
            print('\n')

class CA_Read:
    @staticmethod
    def ca_scan():
        ca_list = [x for x in os.listdir(folder) if x.startswith('CA_') == True]
        print('Checking Account Offers: \n')
        for i in ca_list:
            jsonread = Offer.read_from_json_file(f'{folder}/{i}')
            print('{')
            print(f'"offer_name": "{jsonread.offer_name}",')
            print(f'"amount": {jsonread.amount},')
            print(f'"initial_deposit_amount": {jsonread.initial_deposit_amount},')
            print(f'"account_min_bal": {jsonread.account_min_bal},')
            print(f'"num_monthly_deposits": {jsonread.num_monthly_deposits},')
            print(f'"num_monthly_withdrawals": {jsonread.num_monthly_withdrawals},')
            print(f'"min_monthly_deposit_amount": {jsonread.min_monthly_deposit_amount},')
            print(f'"min_monthly_withdrawal_amount": {jsonread.min_monthly_withdrawal_amount},')
            print(f'"additional_accounts_required": {jsonread.additional_accounts_required},')
            print(f'"issue_date": "{jsonread.issue_date}",')
            print(f'"unacted_expiration_timedelta": "{jsonread.unacted_expiration_timedelta}",')
            print(f'"action_timedelta": "{jsonread.action_timedelta}",')
            print(f'"account_active_age": {jsonread.account_active_age},')
            print(f'"account_dormant_age": {jsonread.account_dormant_age}')
            print('}')
            print('\n')


CC_Read.cc_scan()
SA_Read.sa_scan()
CA_Read.ca_scan()