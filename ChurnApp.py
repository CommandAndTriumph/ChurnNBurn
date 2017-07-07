from flask_json import FlaskJSON, JsonError, json_response, as_json, request
from flask import Flask
from Churn_Models import *
import os
import datetime

app = Flask(__name__)
FlaskJSON(app)

@app.route('/status')
def status():
    return json_response(status = 'Online')

@app.route('/offers')
@app.route('/offers/<offer_type>')
def offers(offer_type= None):
    if str.lower(offer_type) == 'credit':
        churntype = 'CC_'
    elif str.lower(offer_type) == 'savings':
        churntype = 'SA_'
    elif str.lower(offer_type) == 'checking':
        churntype = 'CA_'
    else:
        raise ValueError('You have not selected a valid offer type.')
    return json_response(offer_type = offer_type, offers = [x for x in os.listdir('JSON') if x.startswith(churntype)])

@app.route('/offers/<offer_type>/<offer_name>')
def offer_names(offer_type, offer_name):
    offers = os.listdir('JSON')
    if offer_name not in offers:
        return json_response(offer = None, status_ = 404)
    offer = Offer.read_from_json_file(f'JSON/{offer_name}')


    if offer_type.lower() == 'credit':
        return json_response(offer = {"bonus_amount": offer.amount,
                                      'req_monthly_balance' : offer.balance_amount,
                                      'min_monthly_transactions': offer.minimum_transactions,
                                      'offer_issue_date': datetime.datetime.strftime(offer.issue_date, '%m%d%Y'),
                                      'expiration_timedelta': offer.unacted_expiration_timedelta.days,
                                      'action_timedelta': offer.action_timedelta.days,
                                      'acct_active_age': offer.account_active_age,
                                      'acct_dormant_age': offer.account_dormant_age},
                             status_ = 200)

    if str.lower(offer_type) == 'savings':
        return json_response(offer = {'bonus_amount': offer.amount,
                                      'initial_deposit_amount': offer.deposit_amount,
                                      'min_monthly_deposits': offer.num_monthly_deposits,
                                      'max_monthly_withdrawlas': offer.num_permissible_withdrawals,
                                      'min_account_balance': offer.min_account_balance,
                                      'offer_issue_date': datetime.datetime.strftime(offer.issue_date, '%m%d%Y'),
                                      'expiration_timedelta': offer.unacted_expiration_timedelta.days,
                                      'action_timedelta': offer.action_timedelta.days,
                                      'acct_active_age': offer.account_active_age,
                                      'acct_dormant_age': offer.account_dormant_age},
                                  status_ = 200)

    if str.lower(offer_type) == 'checking':
        return json_response(offer = {'bonus_amount': offer.amount,
                                      'initial_deposit_amount': offer.initial_deposit_amount,
                                      'min_account_balance': offer.account_min_bal,
                                      'min_monthly_deposits': offer.num_monthly_deposits,
                                      'min_monthly_withdrawals': offer.num_monthly_withdrawals,
                                      'min_monthly_deposit_amount': offer.min_monthly_deposit_amount,
                                      'min_monthly_withdrawal_amount': offer.min_monthly_withdrawal_amount,
                                      'additional_accounts_required': offer.additional_accounts_required,
                                      'offer_issue_date': datetime.datetime.strftime(offer.issue_date, '%m%d%Y'),
                                      'expiration_timedelta': offer.unacted_expiration_timedelta.days,
                                      'action_timedelta': offer.action_timedelta.days,
                                      'acct_active_age': offer.account_active_age,
                                      'acct_dormant_age': offer.account_dormant_age},
                             status_ = 200)

@app.route('/offer/<offer_type>', methods = ['POST'])
def offer_input(offer_type):
    req = request.get_json()

    if offer_type.lower() == 'credit':
        offer_name = req["offer_name"]
        amount = req["amount"]
        balance_amount = req["balance_amount"]
        minimum_transactions = req['minimum_transactions']
        issue_date = req['issue_date']
        unacted_expiration_timedelta = req['unacted_expiration_timedelta']
        action_timedelta = req['action_timedelta']
        account_active_age = req['account_active_age']
        account_dormant_age = req['account_dormant_age']
        cc_offer = CC_Offer_Terms(offer_name,
                              amount,
                              balance_amount,
                              minimum_transactions,
                              issue_date,
                              unacted_expiration_timedelta,
                              action_timedelta,
                              account_active_age,
                              account_dormant_age)
        Offer.write_to_json_file(cc_offer, f'JSON/CC_{offer_name}')
        return json_response(created = True, fileName = f'CC_{offer_name}.json', status = 200)

    if offer_type.lower() == 'savings':
        offer_name = req["offer_name"]
        amount = req["amount"]
        deposit_amount = req['deposit_amount']
        num_monthly_deposits = req['num_monthly_deposits']
        num_permissible_withdrawals = req['num_permissible_withdrawals']
        min_account_balance = req['min_account_balance']
        issue_date = req['issue_date']
        unacted_expiration_timedelta = req['unacted_expiration_timedelta']
        action_timedelta = req['action_timedelta']
        account_active_age = req['account_active_age']
        account_dormant_age = req['account_dormant_age']
        sa_offer = SA_Offer_Terms(offer_name,
                                  amount,
                                  deposit_amount,
                                  num_monthly_deposits,
                                  num_permissible_withdrawals,
                                  min_account_balance,
                                  issue_date,
                                  unacted_expiration_timedelta,
                                  action_timedelta,
                                  account_active_age,
                                  account_dormant_age)
        Offer.write_to_json_file(sa_offer, f'JSON/SA_{offer_name}')
        return json_response(created=True, fileName=f'SA_{offer_name}.json', status=200)
    if offer_type.lower() == 'checking':
        offer_name = req["offer_name"]
        amount = req["amount"]
        initial_deposit_amount = req['initial_deposit_amount']
        account_min_bal = req['account_min_bal']
        num_monthly_deposits = req['num_monthly_deposits']
        num_monthly_withdrawals = req['num_monthly_withdrawals']
        min_monthly_deposit_amount = req['min_monthly_deposit_amount']
        min_monthly_withdrawal_amount = req['min_monthly_withdrawal_amount']
        additional_accounts_required = req['additional_accounts_required']
        issue_date = req['issue_date']
        unacted_expiration_timedelta = req['unacted_expiration_timedelta']
        action_timedelta = req['action_timedelta']
        account_active_age = req['account_active_age']
        account_dormant_age = req['account_dormant_age']
        ca_offer = CA_Offer_Terms(offer_name,
                                  amount,
                                  initial_deposit_amount,
                                  account_min_bal,
                                  num_monthly_deposits,
                                  num_monthly_withdrawals,
                                  min_monthly_deposit_amount,
                                  min_monthly_withdrawal_amount,
                                  additional_accounts_required,
                                  issue_date,
                                  unacted_expiration_timedelta,
                                  action_timedelta,
                                  account_active_age,
                                  account_dormant_age)
        Offer.write_to_json_file(ca_offer, f'JSON/CA_{offer_name}')
        return json_response(created=True, fileName=f'CA_{offer_name}.json', status=200)








if __name__ == '__main__':
    app.run()

