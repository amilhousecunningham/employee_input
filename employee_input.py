#!/usr/bin/env python3.6
 
print('Welcome to the new employee registration portal! You wi    ll be prompted to answer 4 questions. There is a 1 question su    rvery is at the end.')

name = input('1. What is your name? ')
birth_date = input('2. What is your birth date? ')
employee_id_number = int(input('3. What is your employee id nu    mber?' ))
age = int(input('4. How old are you? '))

print(f"{name} was born on {birth_date}.")
print(f"{name}'s employee id number is {employee_id_number}.")
print(f"Fun Fact! Half of your age is {age / 2}.")
print(f"Thanks for answering the 4 questions.")

survey = input("Was it easy to answer the questions. Please ty    pe Yes or No. ")
 
print("The survey is now complete.")
