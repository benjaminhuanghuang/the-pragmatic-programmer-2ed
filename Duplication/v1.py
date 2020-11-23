def print_balance(account):

  print("Debits: %10.2f\n", account.debits)
  print("Credits: %10.2f\n", account.credits)
  if account.fees < 0:
    print("Fees: %10.2f-\n", -account.fees)
  else:
    print("Fees: %10.2f\n", account.fees)

  print(" ———-\n")
  if account.balance < 0:
    print("Balance: %10.2f-\n", -account.balance)
  else:
    print("Balance: %10.2f\n", account.balance)


'''
duplication of handling the negative numbers.

repetition of the field width in all the printf calls.
'''