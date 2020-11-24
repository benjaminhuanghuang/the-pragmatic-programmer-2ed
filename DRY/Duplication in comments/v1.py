# Calculate the fees for this account.
#
# * Each returned check costs $20
# * If the account is in overdraft for more than 3 days,
# charge $10 for each day
# * If the average account balance is greater that $2,000
# reduce the fees by 50%
def fees(a):
  f = 0
  if a.returned_check_count > 0:
    f += 20 * a.returned_check_count
  if a.overdraft_days > 3:
    f += 10*a.overdraft_days
  if a.average_balance > 2_000:
    f /= 2
  return f




'''
The intent of this function is given twice: once in the comment and again in
the code.

The comments simply compensates for some bad naming and layout

'''
