def print_balance(account):
  report_line("Debits", format_amount(account.debits))
  report_line("Credits", format_amount(account.credits))
  report_line("Fees", format_amount(account.fees))

  report_line("", " ———-\n")
  report_line("Balance", format_amount(account.balance))


def format_amount(value):
  result = "%10.2f".format(value.abs)
  if value < 0:
    result + "-"
  else:
    result + " "


def report_line(label, amount):
  print_line(label + ":", format_amount(amount))


def print_line(label, value):
  print("%-9s%s\n", label, value)

'''
  what if the client asks for an extra space between the labels and the numbers
'''
