#Write a program that asls the user to enter the monthly costs for the following expenses incurred from operating his or her automobile:
loan payment, insurance, gas, oil, tires, and maintenane. The program should then display the total monthly cost of these expenses, and
the total annual cost of these expenses.


def monthly_cost():
    loan_payment = float(input('Enter your monthly loan payment: '))
    insurance = float(input('Enter your monthly insurance: '))
    gas = float(input('Enter your monthly gas expenses: '))
    oil = float(input('Enter your monthly oil consumption: '))
    tires = float(input('Enter your monthly tire expenses: '))
    maintenance = float(input('Enter your monthly maintenance cost: '))
    monthly_total = loan_payment + insurance + gas + oil + tires + maintenance
    
    print('Your total monthly expenses is', monthly_total)
    
monthly_cost()
