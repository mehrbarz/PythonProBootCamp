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


