# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces


# Create function
def say_hello(name):
    print(f'Hello {name}')

    # say_hello('John Doe')


# Return values
# def get_sum(num, num2):
#     return num + num2


# num = get_sum(2, 3)
# print(num)


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions


def get_sum(num1, num2): return num1 + num2


print(get_sum(3, 5))
