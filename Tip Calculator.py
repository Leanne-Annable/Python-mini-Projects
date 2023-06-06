print("Welcome to the tip calculator!")

bill = float(input("What was the total bill?: £ "))
# this can be converted to any currency and is a float as it allows for decimal places.
tip = int(input("What % would you like to tip?: "))
# you may want to add a note about not inputting % symbol as it needs just numbers to work.
party = int(input("How many people are splitting the bill? "))

tip_percentage = tip / 100
total_tip = bill * tip_percentage
total = bill + total_tip

split_bill = total / party
final_amount = round(split_bill, 2)
final_amount = "{:.2f}".format(split_bill)
# This is stating that we want two decimals in our float, so it will include zeros too.

print(f"Each person should pay: £{final_amount}")
