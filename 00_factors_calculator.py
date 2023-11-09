# Functions go here

# Puts series of symbols at start and end of text
def statement_generator(text, decoration):
    # Make string with five character
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{}  {}  {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# displays instructions / information
def instructions():
    statement_generator("Instruction / Information", "=")
    print()
    print("Please enter a factor")
    print()
    print("This program calculates factors")
    print()
    print("Complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to "
          "quit.")
    print()
    return ""


# checks input is a number more than a given value
def num_check(question):
    valid = False
    while not valid:

        error = "Please enter a factor that is more than " "(or equal to) {}".format(int)

        try:

            # ask user to enter a number
            response = int(input(question))

            # outputs error if input is invalid
            if response < int:
                print(error)

            # checks number is more than zero
            else:
                return response
            print()

        except ValueError:
            print(error)


# gets factors, returns a sorted list
def get_factors():

    # get factors (must be >= 0)
    get_factors() == int("Please enter a factor: ", 0)

    import random

    # set up a list...

    my_list = []

    # generate 4 random numbers between 1 & 10...
    for item in range(0, 4):
        # generate random number between 1 & 10
        random_num = random.randint(1, 10)

        # add number to list
        my_list.append(random_num)

    # print the *unsorted*  list...
    print(my_list)

    # sort the list
    my_list.sort()

    my_list_len = len(my_list)

    # print the sorted list
    print()
    print(my_list)
    print()
    print("The line has {} items".format(my_list_len))

    return ""


# Main Routine goes here

# Heading
statement_generator("Factors Calculator", "-")

# Display instructions if user has not used the program before
first_time = input("Press <enter> to see the instructions or any key to continue")

if first_time == "":
    instructions()

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    comment = ""

    # ask user for number to be factored...
    var_to_factor = num_check("Number?: ")

    if var_to_factor != 1:
        factor_list = get_factors()
    else:
        factor_list = ""
        comment = "One is UNITY!  It only has one factor.  Itself :)"

    # comments for squares / primes
    if len(factor_list) == 2:
        comment = "{} is a prime number.".format(var_to_factor)
    elif len(factor_list) % 2 == 1:
        comment = "{} is a perfect square".format(var_to_factor)

    # output factors and comment

    # Generate heading...
    if var_to_factor == 1:
        heading = "One is special..."

    else:
        heading = "Factors of {}".format(var_to_factor)

    # Output factors and comment
    statement_generator(heading, "*")
    print()
    print(factor_list)
    print(comment)

    print()
    keep_going = input("Press <enter> to continue or any key to quit ")
    print()

print()
print("Thank you for using the factors calculator")
print()
