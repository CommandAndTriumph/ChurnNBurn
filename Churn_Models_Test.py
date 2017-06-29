from Churn_Models import*
import unittest, datetime, os


class test_CC_Offer_Terms(unittest.TestCase):
    def test_json_reading(self):
        offername = 'Chase Freedo000000000000000000m'
        jsonwrite = Offer.write_to_json_file((CC_Offer_Terms(offername, 150, 1000, 4, datetime.datetime.strptime('04202017', '%m%d%Y'), datetime.timedelta(days = float(60)), datetime.timedelta(days = float(30)), 12, 6)), offername)
        jsonread = Offer.read_from_json_file(f'{offername}.json')
        self.assertEqual(offername, jsonread.offer_name)
        self.assertEqual(150, jsonread.amount)
        self.assertEqual(1000, jsonread.balance_amount)
        self.assertEqual(4, jsonread.minimum_transactions)
        self.assertEqual(datetime.datetime.strptime('04202017', '%m%d%Y'), jsonread.issue_date)
        self.assertEqual(datetime.timedelta(days = float(60)), jsonread.unacted_expiration_timedelta)
        self.assertEqual(datetime.timedelta(days = float(30)), jsonread.action_timedelta)
        self.assertEqual(12, jsonread.account_active_age)
        self.assertEqual(6, jsonread.account_dormant_age)
        os.remove(f'{offername}.json')


class test_SA_Offer_Terms(unittest.TestCase):
    def test_json_readwrite(self):
        offername = 'Chase Freedom Savings'
        jsonwrite = Offer.write_to_json_file(SA_Offer_Terms(offername, 200, 10000, 5, 3, 10000, datetime.datetime.strptime('07172017', '%m%d%Y'), datetime.timedelta(days = float(60)), datetime.timedelta(days= float(30)), 12, 6), offername)
        jsonread = Offer.read_from_json_file(f'{offername}.json')
        self.assertEqual(offername, jsonread.offer_name)
        self.assertEqual(200, jsonread.amount)
        self.assertEqual(10000, jsonread.deposit_amount)
        self.assertEqual(5, jsonread.num_monthly_deposits)
        self.assertEqual(3, jsonread.num_permissible_withdrawals)
        self.assertEqual(10000, jsonread.min_account_balance)
        self.assertEqual(datetime.datetime.strptime('07172017', '%m%d%Y'), jsonread.issue_date)
        self.assertEqual(datetime.timedelta(days = float(60)), jsonread.unacted_expiration_timedelta)
        self.assertEqual(datetime.timedelta(days = float(30)), jsonread.action_timedelta)
        self.assertEqual(12, jsonread.account_active_age)
        self.assertEqual(6, jsonread.account_dormant_age)
        os.remove(f'{offername}.json')

class test_CA_Offer_Terms(unittest.TestCase):
    def test_json_readwrite(self):
        offername = 'Chase Freedom Checking'
        jsonwrite = Offer.write_to_json_file(CA_Offer_Terms(offername, 200, 100000, 50000, 5, 10, 2500, 1250, False, datetime.datetime.strptime('04202017', '%m%d%Y'), datetime.timedelta(days = float(60)), datetime.timedelta(days = float(30)), 12, 6), offername)
        jsonread = Offer.read_from_json_file(f'{offername}.json')
        self.assertEqual(offername, jsonread.offer_name)
        self.assertEqual(200, jsonread.amount)
        self.assertEqual(100000, jsonread.initial_deposit_amount)
        self.assertEqual(50000, jsonread.account_min_bal)
        self.assertEqual(5, jsonread.num_monthly_deposits)
        self.assertEqual(10, jsonread.num_monthly_withdrawals)
        self.assertEqual(2500, jsonread.min_monthly_deposit_amount)
        self.assertEqual(1250, jsonread.min_monthly_withdrawal_amount)
        self.assertEqual(False, jsonread.additional_accounts_required)
        self.assertEqual(datetime.datetime.strptime('04202017', '%m%d%Y'), jsonread.issue_date)
        self.assertEqual(datetime.timedelta(days = float(60)), jsonread.unacted_expiration_timedelta)
        self.assertEqual(datetime.timedelta(days = float(30)), jsonread.action_timedelta)
        self.assertEqual(12, jsonread.account_active_age)
        self.assertEqual(6, jsonread.account_dormant_age)
        os.remove(f'{offername}.json')