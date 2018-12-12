
from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey, Date, DateTime, Numeric, Interval, Text, Boolean
from sqlalchemy.orm import mapper
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pathlib import Path
from Churn_Models import*
import datetime
from dateutil.relativedelta import relativedelta
import sqlite3

metadata = MetaData()


credit_card_offer = Table('credit_card_offer', metadata,
    Column('offer_name', Text, primary_key = True),
    Column('amount', Numeric(10,2)),
    Column('balance_amount', Numeric(10,2)),
    Column('minimum_transactions', Integer),
    Column('issue_date', Date, primary_key=True),
    Column('unacted_expiration_timedelta', Interval()),
    Column('action_timedelta', Interval()),
    Column('account_active_age', Interval()),
    Column('account_dormant_age', Interval())
    )

savings_account_offer = Table('savings_account_offer', metadata,
    Column('offer_name', Text, primary_key=True),
    Column('amount', Numeric(10,2)),
    Column('deposit_amount', Numeric(10,2)),
    Column('num_monthly_deposits', Integer),
    Column('num_permissible_withdrawals', Integer),
    Column('min_account_balance', Numeric(10,2)),
    Column('issue_date', Date, primary_key=True),
    Column('unacted_expiration_timedelta', Interval()),
    Column('action_timedelta', Interval()),
    Column('account_active_age', Interval()),
    Column('account_dormant_age', Interval())
    )

checking_account_offer = Table('checking_account_offer', metadata,
    Column('offer_name', Text, primary_key=True),
    Column('amount', Numeric(10, 2)),
    Column('initial_deposit_amount', Numeric(10,2)),
    Column('account_min_bal', Numeric(10,2)),
    Column('num_monthly_deposits', Integer),
    Column('num_monthly_withdrawals', Integer),
    Column('min_monthly_deposit_amount', Numeric(10,2)),
    Column('min_monthly_withdrawal_amount', Numeric(10,2)),
    Column('additional_accounts_required', Boolean),
    Column('issue_date', Date),
    Column('unacted_expiration_timedelta', Interval()),
    Column('action_timedelta', Interval()),
    Column('account_active_age', Interval()),
    Column('account_dormant_age', Interval())
    )



mapper(CC_Offer_Terms, credit_card_offer)
mapper(SA_Offer_Terms, savings_account_offer)
mapper(CA_Offer_Terms, checking_account_offer)
db_file = Path(__file__).parent / 'db.sqlite'
print(f"Obtaining SQLite connection to file {db_file}")

# Note use of three slashes here. See http://docs.sqlalchemy.org/en/latest/core/engines.html
engine = create_engine('sqlite:///' + str(db_file))
Session = sessionmaker(bind=engine)
session = Session()

# print("Creating tables")
# metadata.create_all(bind=engine)
# cco = CC_Offer_Terms('Walls Fergoo Platinum Credit', 200.00, 1000.00, 3, datetime.date(2017,10,23), datetime.timedelta(days= float(60)), datetime.timedelta(days= float(30)), relativedelta(months= 10), relativedelta(months = 5))
# sao = SA_Offer_Terms('True West Super Plus Foogoo', 125.00, 500.00, 2, 2, 500.00, datetime.date(2017,10,25), datetime.timedelta(days= float(90)), datetime.timedelta(days= float(45)), relativedelta(months= 8), relativedelta(months = 4))
# cao = CA_Offer_Terms('Chase Choosy Chicken for Farmers Plus', 200.00, 10000.00, 10000.00, 3, 6, 1000.00, 500.00, False, datetime.date(2017,8,20), datetime.timedelta(days= float(65)), datetime.timedelta(days= float(30)), relativedelta(months= 12), relativedelta(months = 6))
#
# print(f"Created offer: {cco}")
# print(f"Created offer: {sao}")
# print(f"Created offer: {cao}")
# session.add(cco)
# session.add(sao)
# session.add(cao)
# print(f"Added to session")
# session.commit()
# print(f"Committed")