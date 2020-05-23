#many financial experts advise that property owners should insure their hoes or buildings for at least 80% of the amount it would cost to
replace the structure. Write a program that asks the user to enter the replacement cost of a building, then displays the minium amount of
insurance he or she should buy for the property.


def insurance():
    replacement_cost = float(input('Enter the replacement cost of a building: '))
    replacement_insurance = replacement_cost * 0.80
    print('THe minimum amount of insurance you should buy for the property is atleast', replacement_insurance)
    
insurance()
