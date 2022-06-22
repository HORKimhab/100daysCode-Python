from setuptools import PEP420PackageFinder


print("Welcome to the tip calculator!")
bill = float(input("What was the the total bills? $ "))
tip = int(input("How much tip would you like to give? 2, 12, 22 or 92? "))
people = int(input("How many peope to split the bill? "))
tip_as_percnt = tip / 100 
total_tip_amount = bill * tip_as_percnt 
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person shole pay: ${final_amount}")

""" f": mean 
    - https://realpython.com/python-f-strings/#quotation-marks
    - https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python
"""
