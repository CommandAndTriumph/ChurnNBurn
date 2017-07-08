import sys, datetime, re
from Churn_Models import*
from dateutil.relativedelta import relativedelta
offer_name = sys.argv[1]
application_date = datetime.datetime.strptime(sys.argv[2], '%Y-%m-%d')
jsonread = Offer.read_from_json_file(f'JSON/{offer_name}.json')
offer_name_simp = re.sub('(CC_|SA_|CA_)', '', offer_name)
if offer_name.startswith('CC_') == True:
    offer_type = 'credit card'
    offer_type_caps = 'Credit card'
elif offer_name.startswith('SA_') == True:
    offer_type = 'savings account'
    offer_type_caps = 'Savings account'
elif offer_name.startswith('CA_') ==  True:
    offer_type = 'checking account'
    offer_type_caps = 'Checking account'
formatted_issue_date = jsonread.issue_date.strftime('%Y-%m-%d')
formatted_application_date = application_date.strftime('%Y-%m-%d')
print(f'{formatted_issue_date} * Offer for {offer_name_simp} {offer_type} issued')
print('           |')
print('           |')
if jsonread.issue_date > application_date:
    print('This offer has not been issued yet')
elif jsonread.issue_date + jsonread.unacted_expiration_timedelta + jsonread.action_timedelta >= application_date:
    print(f'{formatted_application_date} * Application submitted (hypothetical)')
else:
    print('Offer has already expired.')

offer_to_completion_timedelta = relativedelta(months = jsonread.account_active_age)
offer_post_completion_timedelta = relativedelta(months = jsonread.account_dormant_age)
offer_completion_date = application_date + offer_to_completion_timedelta
offer_post_completion_date = offer_completion_date + offer_post_completion_timedelta
offer_completion_date_formatted = datetime.datetime.strftime(offer_completion_date, '%Y-%m-%d')
offer_post_completion_date_formatted = datetime.datetime.strftime(offer_post_completion_date, '%Y-%m-%d')
print('           |')
print('           |')
print(f'{offer_completion_date_formatted} * Deadline to complete to receive bonus (${int(jsonread.amount)})')
print('           |')
print('           |')
print(f'{offer_post_completion_date_formatted} * {offer_type_caps} may be cancelled')






