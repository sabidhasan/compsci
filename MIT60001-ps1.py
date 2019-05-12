#################
#    ps1a.py    #
# House Hunting #
#################
PORTION_DOWN_PAYMENT = 0.25

def integer_input(msg):
  while True:
    try:
      return int(input(msg))
    except:
      print("Value must be an integer number")
      continue
    
total_cost = integer_input('What is the cost for the home? ')
portion_saved = integer_input('What percentage of salary needs to be saved? ') / 100
annual_salary = integer_input('What is your starting annual salary? ')
current_savings = 0
annual_return = 0.04

month = 0
while current_savings < total_cost * PORTION_DOWN_PAYMENT:
  current_savings += (annual_salary / 12 * portion_saved) + (current_savings * annual_return / 12)
  month += 1

print ("It will take you", month, "months to save for the down payment.")


#################
#    ps2a.py    #
# House Hunting #
#################
total_cost = integer_input('What is the cost for the home? ')
annual_salary = integer_input('What is your starting annual salary? ')
portion_saved = integer_input('What percentage of salary needs to be saved? ') / 100
semiannual_raise = integer_input('What percentage is the semi-annual salary raise? ') / 100
annual_return = 0.04
current_savings = 0

month = 0
while current_savings < total_cost * PORTION_DOWN_PAYMENT:
  current_savings += (annual_salary / 12 * portion_saved) + (current_savings * annual_return / 12)
  month += 1
  
  if ((month + 1) % 6 == 0):
    annual_salary *= (1 + semiannual_raise)

print ("It will take you", month, "months to save for the down payment.")