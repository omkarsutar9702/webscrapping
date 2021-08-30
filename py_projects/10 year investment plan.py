import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#create list
year =[]
yearly_income =[]
yearly_investment =[]
yearly_expenses =[]
annual_returns =[]

#yearly constent income
Income = 50000
#yearly constent expences 
Expense = Income / 2
#average intrest of 8% per year
intrest_rate = 0.05
#you invest half of your income
investment = Income / 2
#calculating the annual return 
annual_return = investment * intrest_rate
#getting current year
Year = 2021

year.append(Year)
yearly_income.append(Income)
yearly_expenses.append(Expense)
yearly_investment.append(investment)
annual_returns.append(annual_return)

#loop for n years
invested_years = 20 
for i in range (0, invested_years-1):
  # update the investment to be the previous investment plus 
  #the previous annual returns plus half of your income
  investment = investment + annual_return + Income /2 
  #update the annual return to be the current investment times the intrest rate 
  annual_return = investment * intrest_rate
  #append the new data into the lists 
  year.append(Year+i+1)
  yearly_income.append(Income)
  yearly_expenses.append(Expense)
  yearly_investment.append(investment)
  annual_returns.append(annual_return)
  
#create the data frame 
df = pd.DataFrame()
df['year'] = year
df['yearly income'] = yearly_income
df['yearly expenses'] = yearly_expenses
df['yearly investment'] = yearly_investment
df['annual returns'] = annual_returns

print(df.head())

#visually show the data 
plt.figure (figsize=(15,7))
plt.plot(df['year'],df['yearly expenses'],label='yearly expenses')
plt.plot(df['year'],df['annual returns'],label='annual returns')
plt.title('returns in 10 years')
plt.xlabel('years')
plt.ylabel('INR')
plt.xticks(df['year'])
plt.legend()
plt.show()