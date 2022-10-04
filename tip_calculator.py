print("Welcome to the tip calculator")
bill = input("What was the total bill? ")
tip = input("What percentage tip you want to give? 10, 12, or 15? ")
number_of_people = input("How many people to split the bill? ")

bill_as_float = float(bill)
tip_as_float = float(tip)
number_of_people_as_int = int(number_of_people)

total = (bill_as_float * (tip_as_float / 100)) + bill_as_float
amouunt_per_person = total / number_of_people_as_int

result_per_person = round(amouunt_per_person, 2)

result_per_person = "{:.2f}".format(amouunt_per_person)

print(f"each person should pay: ${result_per_person}")