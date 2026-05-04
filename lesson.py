# PRINT FUNCTION 

print('hello world')
print('My favoruite food is Fried Chicken', 'Ice Cream', 'Fried Fish')

#  Understanding Variables and Data Types

my_integer_var = 10
print('Integer:', my_integer_var)
print(type(my_integer_var))

my_float_var = 4.50
print('Float:', my_float_var)
print(type(my_float_var))

my_string_var = 'Hello, World!'
print('String:', my_string_var)
print(type(my_string_var))

my_boolean_var = True
print('Boolean:', my_boolean_var)
print(type(my_boolean_var))

my_set_var = {7, 'hello', 8.5}
print('Set:', my_set_var)
print(type(my_set_var))

my_dictionary_var = {'name': 'Alice', 'age': 25}
print('Dictionary:', my_dictionary_var)
print(type(my_dictionary_var))

my_tuple_var = {7, 'hello', 8.5}
print("Set:", my_tuple_var)
print(type(my_tuple_var))

my_range_var = range(5)
print('Range:', my_range_var)
print(type(my_range_var))

my_list = [22, 'Hello World!', 3.14, True]
print(my_list)
print(type(my_list))

my_var_1 = 'Hello World!'
my_var_2 = 21
print(type(my_var_1))
print(type(my_var_2))

print(isinstance('Hello World', str))
print(isinstance(True, bool))
print(isinstance(42, int))
print(isinstance('John Doe', int))

name = input("what's your name? ")
print('Hello,', name)

name = input("what's your name? ")
print('Hello,', end="", sep="")
print(name)

name = input("what's your name? ")
name = name.strip().title()
print(f'Hello, {name}')

name = input("what's your name? ").strip().title()
first, last = name.split()
print(f'Hello, {name}')

def hello(to="world"):
    print("hello,", to)

hello()
name = input("What's your name? ")
hello(name)

def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()