from flask_json import FlaskJSON, JsonError, json_response, as_json
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


if __name__ == '__main__':
    app.run()

