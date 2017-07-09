create table if not exists credit_card_offer (
    offer_name text,
    amount real,
    balance_amount real,
    minimum_transactions int,
    issue_date text,
    unacted_expiration_timedelta text,
    action_timedelta text,
    account_active_age int,
    account_dormant_age int
    );

create table if not exists savings_account_offer (
    offer_name text,
    amount real,
    deposit_amount real,
    num_monthly_deposits int,
    num_permissible_withdrawals int,
    min_account_balance real,
    issue_date text,
    unacted_expiration_timedelta text,
    action_timedelta text,
    account_active_age int,
    account_dormant_age int
    );
    
create table if not exists checking_account_offer (
    offer_name text,
    amount real,
    initial_deposit_amount real,
    account_min_bal real,
    num_monthly_deposits int,
    num_monthly_withdrawals int,
    min_monthly_deposit_amount real,
    min_monthly_withdrawal_amount real,
    additional_accounts_required int,
    issue_date text,
    unacted_expiration_timedelta text,
    action_timedelta text,
    account_active_age int,
    account_dormant_age int
    );
    


