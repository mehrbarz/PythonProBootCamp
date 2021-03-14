print("great"[4])
#Integer

#the comiler removes the underscore
432_322_333

#Boolean
True
False

#Type casting
num_char = len(input("What is your name? "))
new_num_char = str(num_char)
print("Your name contains "+ new_num_char + " characters")

#day2-1 exercise
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
print(type(two_digit_number))

print(two_digit_number[0])

digitsAdded = int(two_digit_number[0]) + int(two_digit_number[1])
print(digitsAdded)


#Exercise 2-2 BMI
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = (int(weight) / (float(height) **2 ))
print(int(BMI))

#round 
print(round(4.555555 , 2))

#floor division
print(8 // 3)

#f-string
score = 4
kilometers = 32
isWinner = True

print(f"Your score is {score} at the distance of {kilometers} km and you are a {isWinner} winner." )


#Life in weeks
age = input('what is your age? ')
age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining *12 

print(months_remaining)
print(f'You have {days_remaining} days and {weeks_remaining} weeks remaining to be 90 years old.')






