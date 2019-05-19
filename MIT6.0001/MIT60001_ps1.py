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

#################
#    ps3a.py    #
# House Hunting #
#################
total_cost = 1000000
annual_salary = integer_input('What is your starting annual salary? ')
semiannual_raise = 7 / 100
annual_return = 0.04

def savings_in_36_months(salary, portion_saved, ann_ret):
  # Determine savings in 36 months, based on annual salary, portion saved and rate of return
  curr_sav = 0
  for i in range(36):
    curr_sav += (salary / 12 * portion_saved / 10000) + (curr_sav * ann_ret / 12)
    # Give raise if necessary
    if ((i + 1) % 6 == 0):
        salary *= (1 + semiannual_raise)
  return curr_sav


test_range = range(10000)
iterations = 0
while len(test_range) > 2:
  portion_saved = test_range[int(len(test_range) / 2)]

  # Check saving with this rate at 36 months
  current_savings = savings_in_36_months(annual_salary, portion_saved, annual_return)

  if abs(current_savings - (total_cost * PORTION_DOWN_PAYMENT)) < 100:
    print('we found the optimal rate', portion_saved, ' in ', iterations + 1, ' iterations.')
    break
  elif current_savings < (total_cost * PORTION_DOWN_PAYMENT):
    # Reattempt with higher rate
    test_range = test_range[int(len(test_range) / 2):]
  elif current_savings > total_cost * PORTION_DOWN_PAYMENT:
    test_range = test_range[:int(len(test_range) / 2)]

  iterations += 1

if len(test_range) <= 2:
  print ("It is not possible to pay the down payment in three years.")
