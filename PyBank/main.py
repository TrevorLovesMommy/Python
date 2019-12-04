import pandas as pd
import numpy as np

# Store filepath in a variable
path = "Resources/budget_data.csv"

 # Read our Data file with the pandas library
df = pd.read_csv(path, encoding="ISO-8859-1")

# Total num of months
months = df["Date"].nunique()

# net P&L
p_and_l = df["Profit/Losses"].sum()

#get number of rows in Profit/Losses column
num_rows = len(df["Profit/Losses"])

#add a new column to data frame with monthly dollar changes.  
#there will be a null value for the first month
for i in range(0,num_rows):
    if i<(num_rows-1):
        df.loc[i+1,"Change"]= (df["Profit/Losses"][i+1]) - (df["Profit/Losses"][i])

#get mean, max and min of monthly dollar changes
mean_change = df["Change"].mean()
min_change = df["Change"].min()
max_change = df["Change"].max()

#get the row of max and min dollar changes
min_change_row = (df["Change"].idxmin())
max_change_row = (df["Change"].idxmax())

# get corresponding month of max and min changes
min_month = df.loc[min_change_row, "Date"]
max_month = df.loc[max_change_row, "Date"]

#print output
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {months}")
print(f"Total:  ${p_and_l}")
print("Average Change:  $" + format (mean_change, ".2f"))
print("Greatest Increase in Profits:  " + max_month + " ($" + format(max_change, ".0f") + ")")
print("Greatest Decrease in Profits:  " + min_month + " ($" + format(min_change, ".0f") + ")")

##Print to text file
#print("Financial Analysis", file=open("pybank_output.txt", "a"))
print("Financial Analysis", file=open("pybank_output.txt", "a"))
print("----------------------------", file=open("pybank_output.txt", "a"))
print(f"Total Months:  {months}", file=open("pybank_output.txt", "a"))
print(f"Total:  ${p_and_l}", file=open("pybank_output.txt", "a"))
print("Average Change:  $" + format (mean_change, ".2f"), file=open("pybank_output.txt", "a"))
print("Greatest Increase in Profits:  " + max_month + " ($" + format(max_change, ".0f") + ")", file=open("pybank_output.txt", "a"))
print("Greatest Decrease in Profits:  " + min_month + " ($" + format(min_change, ".0f") + ")", file=open("pybank_output.txt", "a"))








# get min profit
#idmin, axis = 0  returns index of the row
#.loc returns the row of the above index
#min_profit_df = budget_data_df.loc[budget_data_df["Profit/Losses"].idxmin(axis = 0)]
#min_profit_month = min_profit_df[0]
#min_profit_value = min_profit_df[1]
# average change
#average_change = budget_data_df["Profit/Losses"].mean()

# get max profit
#idxmax, axis = 0  returns index of the row
#.loc returns the row of the above index
#max_profit_df = budget_data_df.loc[budget_data_df["Profit/Losses"].idxmax(axis = 0)]
#max_profit_month = max_profit_df[0]
#max_profit_value = max_profit_df[1]

#print(len(df["Profit/Losses"]))
#print(df["Profit/Losses"][1])
#print("----------------------------")
#calc average change
#dollar_change = []
#pandas.DataFrame.append()
#avg_dollar_change = average(dollar_change)
#mean_dollar_change = np.mean(dollar_change)
#max_dollar_change = np.max(dollar_change)
#min_dollar_change = np.min(dollar_change)
#
#print(mean_dollar_change)
#print(max_dollar_change)
#print(min_dollar_change)

