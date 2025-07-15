# input("What was the total bill?")

print("Welcome to the tip calculator!!")
Total_Bill = float(input("What was the total bill?"))
Tip = float(input("What percent of tip would you like to give?"))
Chop = float(input( "How many people to split the bill?"))
Final_Bill = round(float(Total_Bill * (Tip/100) + Total_Bill) / Chop, 2)

print(f"Your share of the bill is...${Final_Bill}")




