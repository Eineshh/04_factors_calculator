import random


# Puts a series of symbols at the start and end of text
def statement_generator(text, decoration):
    ends = decoration * 5
    statement = "{}  {}  {}".format(ends, text, ends)
    print()
    print(statement)
    print()


# Displays instructions / information
def instructions():
    statement_generator("Instruction / Information", "=")
    print("\nPlease enter a factor.")
    print("\nThis program calculates factors.")
    print(
        "\nComplete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to quit.")
    print()


# Checks input is a number more than a given value
def num_check(question):
    while True:
        try:
            response = int(input(question))
            if response <= 0:
                print("Please enter a factor that is greater than 0.")
            else:
                return response
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Gets factors and returns a sorted list
def get_factors():
    # Get factors (must be >= 0)
    input_factor = num_check("Please enter a factor: ")

    # Set up a list...
    my_list = []

    # Generate 4 random numbers between 1 & 10...

