Boolean Type
Boolean is a data type that can hold one of two values, True and False (always capitalized!). They’re the building blocks for complex logical operations, and serve as the basis for decision-making in programming. For example, let’s imagine a lamp that can be either on or off:

is_light_on = True
print(is_light_on) # True

The is_light_on variable reflects the lamp’s state. We assigned it the value True, meaning the lamp is currently on, and could be switched off:

is_light_on = True
print(is_light_on) # True

is_light_on = False
print(is_light_on) # False

We can obtain a boolean value by comparison, too — using comparison operators:

== — strict equality
!= — strict inequality
< — less than
> — greater than
<= — less than or equal to
>= — greater than or equal to
…for example:

print(5 == 5) # True
print(5 < 10) # True
print(5 > 10) # False


We aren’t declaring a new variable, but asking Python to check whether the two numbers are equal, hence, the two equal signs — rather than one. Here’s another such example:

apple = 5
pear = 5
orange = 10

print(apple == pear) # True
print(pear < orange) # True
print(apple > orange) # False


------------Logical Constructs with Multiple Conditions
Having discovered all the logical operators, we can now create complex logical constructs. For instance, let’s imagine we’re deciding whom to invite for our upcoming party, and we’re after two kinds of people — those who live nearby or aren’t busy at that time. Then also, the guest must either be our friend. Here’s the code:

is_busy = False
lives_nearby = True
is_friend = True


We’ll save our decision for every guest in the should_invite variable:

should_invite = not is_busy or lives_nearby and is_friend
print(should_invite) # True


should_invite = not is_busy or lives_nearby and is_friend
print(should_invite) # True



To set the priority of operations, you can use parentheses, which will affect the result:

should_invite = not (is_busy or lives_nearby) and is_friend
#		  not (False or True) and True
#		  not  True and True
#		         False and True
# 	    	         False


Now, the condition is no longer met (False), because we set priority with parentheses.








