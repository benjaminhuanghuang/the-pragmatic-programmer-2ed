def calculate_account_fees(account):
  fees = 20 * account.returned_check_count
  if account.overdraft_days > 3:
    fees += 10 * account.overdraft_days 
  if account.average_balance > 2_000:
    fees /= 2 
  return fees