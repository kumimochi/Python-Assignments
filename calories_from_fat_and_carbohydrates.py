#A nutritionist who works for a fitness club helps members by evaluating their diets. As part of her evaluation, she asks members for the
number of fat grams and carbohydrate grams that they consumed in a day. Then, she calculates the number of calories that result from the
fat, using the following formula:


def calories():
    fat_grams = float(input('Enter the number of fat in grams: '))
    carbs_grams = float(input('Enter the number of carbohydrate in grams: '))
    calories_from_fat = fat_grams * 9
    calories_from_carbohydrates = carbs_grams * 4
    print('Your fat consumption is', calories_from_fat, 'and your carbohydrates consumption is', calories_from_carbohydrates)

calories()
