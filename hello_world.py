#!/bin/python3

name = ""
age = ""
degree_program = ""

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
degree_program = input("Please enter your degree program: ")

remaining_age = (age * 3) % 2

print("Hi my name is "+ name + ". My remaining age is "+ str(remaining_age) + " and I am majoring in " + degree_program + " at NOVA.")
