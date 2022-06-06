###########
print("\nPart 1")
###########

# Functions separate your code into smaller parts.
# They are used to perform specific tasks.
# Use functions to make your code more readable, and avoid repeating yourself.
# 'print' is an example of a "built-in" function.

# For example, if we wanted to print greetings for several people, we could use a function.
# Here's what the code looks like without a function:
name = "Alice"
print("Hello", name)

name = "Bob"
print("Hello", name)

name = "Elijah"
print("Hello", name)

print() # print a blank line

# But this is hard to read and hard to change.
# What if we wanted to say "Hey" instead of "Hello"?
# We can make it better by using a function.

# Funcions are defined with the "def" keyword. Next is the name of the function, followed by parentheses.
# The parentheses contain the arguments that the function takes in.
# Code inside a function is indented. This is called a "block". The function ends by unindenting.
# Here's an example:

def say_greeting_to(name):
    print("Hello", name)

# we can "call" the function like this:
say_greeting_to("Alice")
say_greeting_to("Bob")
say_greeting_to("Elijah")

# the output is exactly the same as the previous example, but we can change the greeting more easily.
# notice how the important part of the program is only repeated once 'print("Hello", name)'
# try changing the say_greeting_to function to print "Hey ____" instead of "Hello ____".


###########
print("\nPart 2")
###########

# Functions take in "arguments" and they "return" values.
# Arguments are the values that are passed into the function.
# Return values are the variables that are returned by the function.

# In the previous example, we passed in "name" as an argument.
# There was no return value, so the function returned None, which is a special value meaning nothing is stored.
# But if we wanted to return a value, we could do so with the return statement.
# Here's an example:

def get_greeting_for(name):
    return "Hello " + name + ", it's nice to meet you!"

# now, if we call this function, nothing happens because we are not displaying the return value.
get_greeting_for("Alice") # returns "Hello Alice, it's nice to meet you!" but nothing is displayed.

# we can display it by storing the return value in a variable:

greeting = get_greeting_for("Bob")
print(greeting)


# try defining your own function to say goodbye to a person. Use a return statement to return a value, then print the value.
...
