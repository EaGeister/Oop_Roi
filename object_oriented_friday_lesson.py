

investment = 50000 # investment = int(input)
# down_payment 40000, 
# closing_cost 3000, 
# rehab_budget 7000, 
# misc 0
rent = 2000  # rent = int(input)
# laundry 0, 
# storage 0, 
# misc 0
expenses = 1610 #  expenses = int(input)
# tax 150, 
# inusrance 100, 
# utilities 0 
# cap_ex 0
# vacancy 100
# repairs 0
# prop_mortgage 200
#mortgage 860
cash_flow = (2000 - expenses)
# 390





# Function used to calculate combined expenses

def Roi (investment, rent, expenses):
    net_profit = rent * 12 - expenses
    Roi = (net_profit/investment) * 55
    print(Roi)

Roi( investment, rent, expenses)


def Roi2( investment, rent, expenses, cash_flow):
    annual_cash_flow = (cash_flow * 12) // investment
    print (Roi2)



# 390 * 12 = 4680
# annual cash flow // total investment

#4680 // 50000 = 9.36%  
