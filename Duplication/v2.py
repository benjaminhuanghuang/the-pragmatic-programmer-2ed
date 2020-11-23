def print_balance(account):

  print("Debits: %s\n", format_amount(account.debits))
  print("Credits: %s\n", format_amount(account.credits))
  print("Fees: %s\n", format_amount(account.fees))

  print(" ———-\n")
  print("Balance: %s\n", format_amount(account.balance))

def format_amount(value):
  result = "%10.2f".format(value.abs)
  if value < 0:
    result + "-"
  else:
    result + " "

'''
  what if the client asks for an extra space between the labels and the numbers
'''