import pandas as pd

# Store filepath in a variable
budget_data = "Resources/budget_data.csv"

 # Read our Data file with the pandas library
budget_data_df = pd.read_csv(budget_data, encoding="ISO-8859-1")

# Total num of months
months = budget_data_df["Date"].nunique()

# net P&L
p_and_l = budget_data_df["Profit/Losses"].sum()

# average change
average_change = budget_data_df["Profit/Losses"].mean()

# get max profit
#idxmax, axis = 0  returns index of the row
#.loc returns the row of the above index
max_profit_df = budget_data_df.loc[budget_data_df["Profit/Losses"].idxmax(axis = 0)]
max_profit_month = max_profit_df[0]
max_profit_value = max_profit_df[1]

# get min profit
#idmin, axis = 0  returns index of the row
#.loc returns the row of the above index
min_profit_df = budget_data_df.loc[budget_data_df["Profit/Losses"].idxmin(axis = 0)]
min_profit_month = min_profit_df[0]
min_profit_value = min_profit_df[1]

print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {months}")
print(f"Total:  ${p_and_l}")
print("Average Change:  $" + format (average_change, ".2f"))
print(f"Greatest Increase in Profits:  {max_profit_month} $({max_profit_value})")
print(f"Greatest Decrease in Profits:  {min_profit_month} $({min_profit_value})")

#Print to text file
print("Financial Analysis", file=open("pybank_output.txt", "a"))
print("----------------------------", file=open("pybank_output.txt", "a"))
print(f"Total Months:  {months}", file=open("pybank_output.txt", "a"))
print(f"Total:  ${p_and_l}", file=open("pybank_output.txt", "a"))
print("Average Change:  $" + format (average_change, ".2f"), file=open("pybank_output.txt", "a"))
print(f"Greatest Increase in Profits:  {max_profit_month} $({max_profit_value})", file=open("pybank_output.txt", "a"))
print(f"Greatest Decrease in Profits:  {min_profit_month} $({min_profit_value})", file=open("pybank_output.txt", "a"))

