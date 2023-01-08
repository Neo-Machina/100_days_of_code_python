# You are going to write a program that will select a random name from a list of names.
# The person selected will have to pay for everybody's food bill.

import random 

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

random_index = random.randrange(len(names))
random_person = names[random_index]
print(f'{random_person} is going to buy the meal today!')