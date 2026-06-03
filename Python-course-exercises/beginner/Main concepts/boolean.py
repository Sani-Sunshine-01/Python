'''
The program on the screen checks whether a certain person is an adult.

Assign your age to the variable age.
Use print() to display the result of the program on the screen.
'''

age = 20
is_adult = age >= 18

print(is_adult)
#  Write code here



#------------ LOGICKI OPERATORI -------------

#TASKI1
'''
On the screen you can see the is_light_on variable. Using print()
 and the logical operator not, change the value of the is_light_on variable to the opposite.'''
is_light_on = True
#  Write code here

print(not is_light_on)


#TASK2

# change code below this line

is_holiday = True
is_vacation = False

# change code above this line

can_stay_home = is_holiday or is_vacation  # don't change this line


#TASK3

'''
There are three variables:

is_water_hot indicates the availability of hot water.
have_tea indicates the availability of tea.
can_make_tea indicates the availability of both ingredients.
Change either is_water_hot or have_tea so that can_make_tea is False.
'''

# change code below this line

is_water_hot = True
have_tea = False

# change code above this line

can_make_tea = is_water_hot and have_tea  # don't change this line


#--------------MULTIPLE CONDITIONS ---------------------

'''Our code contains four variables:

has_eggs indicating the availability of eggs.
has_flour indicating the availability of flour.
has_sugar indicating the availability of sugar.
can_make_cake indicating if all ingredients are available:
Change the values of has_flour and has_sugar so that can_make_cake turns True.
'''


has_eggs = True
has_flour =True
has_sugar = True


can_make_cake = has_eggs and has_flour and has_sugar  # don't change this line

#task

'''
A worker can go home if they:

finished the planned work for the day (variable work_done);
OR the workday is over (variable day_finished).
Create a variable can_go_home that will check if the worker can go home. 
Print the result to the console using print.
'''


work_done = True
day_finished = False

#  Write code here
can_go_home=work_done or day_finished

print(can_go_home)