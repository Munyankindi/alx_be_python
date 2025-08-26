income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = income - expenses
annual_interest_rate = 0.05
annual_projected_savings = float(monthly_savings * 12 + (monthly_savings * 12 * annual_interest_rate))
print("Your monthly savings are : ",monthly_savings)
print("projected savings after one year,with interest, is : ",annual_projected_savings)
