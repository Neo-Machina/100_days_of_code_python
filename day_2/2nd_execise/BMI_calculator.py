# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

float_height = float(height)
int_weight = int(weight)

operation = int_weight / (float_height ** 2)

int_operation = int(operation)

print(int_operation)