#The .lower() and .upper() Methods

#task1

'''In this task, you'll work with the variable first_name.

Assign a value to this variable. This value should be a string containing your name. Don't forget that strings are written in quotation marks.
Use the .lower() method to lowercase the name stored in that variable.
Print the result on the screen using the print() function.'''

first_name = "Sani"
first_name_lower=first_name.lower()

print(first_name_lower)


#TASK2

'''Use the variable last_name. Write your last name into it. Don't forget that strings are written in quotes.

Next, use the .upper() method to convert your last name to uppercase.

Finally, use the print() function to print the new value to the screen.'''

last_name = "Sani"

last_name_upper=last_name.upper()

print(last_name_upper)



## CONCATENTATION

# Concatenation is a fancy programming term for “adding words together.” 
# It’s used, for instance, in forms, where we’re asked to input our name and surname, 
# which the program then combines and shows as a single string. We just need the + sign

'''Declare a variable result_string.
Concatenate the values of variables a, b and c to receive the string "Concatenation".
Use the print function to display the result_string.'''

a = "Con"
b = "enation"
c = "cat"

result_string= a+c+b

print(result_string)



### STRING INTERPOLATION

'''two variables for you.

a with the word Hello;
b with the word world.
Interpolate them to get "Hello, world!". To do so:

Declare a variable result_string.
Combine a space, a comma, an exclamation mark, a and b to arrive at the target string.
Use the print function to display result_string on the screen.
💡 Feel free to use interpolation (f-strings).'''


a = "Hello"
b = "world"
# write your code below this line

result_string=f"{a}, {b}!"



#GREETING CONCAT

'''Create a variable first_name and give it the value of your first name.
Create a greeting variable and use concatenation to write the greeting Hello, name!
Use the print() function to display the result on the screen.
💡 Don't forget about punctuation marks and spaces.'''

first_name = "name"
greeting = "Hello, " + first_name + "!"
print(greeting)


#This method (CONCAT) works fine as long as there are few parts to concatenate. 
# If, say, we wanted to create a greeting — like “Hello, Bruce Wayne. 
# Welcome, hero” — we’d need to add spaces, commas and a period in between. All wrapped in quotes.

#GREETING INTERPOLATION

first_name="name"
greeting=f"Hello, {first_name}!"
print(greeting)



### String Length and Character Index ###

#TASK
goal = "Help 1 million people worldwide build their careers in Tech."

goal_length=len(goal)
print(goal_length)


#INDEX

goal = "Help 1 million people worldwide build their careers in Tech."

index=goal[5]

print(index)


#GET THE LAST CHARACTER OF STRING
''' Using ---the word variable.

Use the built-in len() function to determine the number of characters in the word string.

Use the length to find the last character of the string. Store the last character in the last_char variable.

Use print() to display last_char on the screen.'''

word = "Programming"

length = len(word)
index = length - 1

last_char = word[index]

print(last_char)


