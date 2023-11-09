# checks input is a number more than a given value
def num_check(question):
    valid = False
    while not valid:

        error = "Please enter a factor that is more than " "(or equal to) {}".format(int)

        try:

            # ask user to enter a number
            response = int(input(question))

            # checks number is more than zero
            if not response < int:
                return response

            # outputs error if input is invalid
            else:
                print(error)
            print()

        except ValueError:
            print(error)
