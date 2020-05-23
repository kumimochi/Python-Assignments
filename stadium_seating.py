#Chapter 5
#Starting Out with Python, Global Edition, 4th Ed

#There are three seating categories at a stadium. Class A seats costs $20, Class B seats cost $15, and Class C seats costs $10. Write a
#program that asks how many tickets for each class of seats were sold, then displays the amount of income generated from ticket sales.

class_a = float(input('Enter the number of tickets sold for Class A: '))
class_b = float(input('Enter the number of tickets sold for Class B: '))
class_c = float(input('Enter the number of tickets sold for Class C: '))

def total_cost(class_a, class_b, class_c):
    a = class_a * 20
    b = class_b * 15
    c = class_c * 10
    
    print('The total amount of the income generated from ticket sales is $', a + b + c, sep='')
    
total_cost(class_a, class_b, class_c)
