#Basics_assign values

first_name = "Sun"
age = 33
weight =80.7
is_married = False


#Numbers - ADDITION AND SUBSTRACTION

#task1
length = 5
width = 3

amount=length+width
difference=length - width

#task2

length = 5
width = 3

amount=length+width
difference=length - width

print(amount)
print (difference)


#MULTIPLY AND DIVIDE

#task1
length = 8
width = 9
#  Write code here

multiplication=length*width
division= length/width

print("Multiplication of length and width:", multiplication)
print("Division of lenght and width",division)

#OPERATOR PRECEDENCE

#Per operator precedence, multiplication is performed first, addition second. It’s just like in math, where multiplication and division come first, addition and subtraction — second. And just like in math, 
# we can change this order using parentheses ()

total_cost = 3 * (50 + 120)
print(total_cost) # 510

#Data type- FLOAT

#task-shopping budget using float

budget = 50
milk_price = 3
bread_price = 2

rest=budget-(milk_price+bread_price)


#task-money to spend 
#John earned 1,000,000 last year.
#Write a program that will calculate how much he earned daily.

yearly_salary = 1000000

daily_earnings=yearly_salary/365



#task - RECTANGLE 

#You plan to plant a garden 🌳
#To do this, you need to calculate its area.
#The garden is in the shape of a rectangle. Declare a new variable area and calculate the area of the garden. Use the variables 
#length to denote the length and width to denote the width.

length = 20
width = 10

area=length*width


'''You want to study 6 days a week for 2 hours daily from your computer (study_hours_computer) and 1 hour on your way home in the metro from your phone (study_hours_phone).

Write a program that will calculate the total number of hours dedicated to studying (per week). Use print to display the result.'''

study_hours_computer = 2
study_hours_phone = 1
study_days = 6

total_hours=study_days*(study_hours_computer+study_hours_phone)
print(total_hours)