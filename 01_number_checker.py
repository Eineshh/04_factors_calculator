# checks input is a number more than a given value
def num_check(question, low):
    valid = False
    while not valid:

        error = "Please enter a integer that is more than (or equal to) {}".format(low)

        try:

            # ask user to enter a number
            response = int(input(question))

            # checks number is more than, or equal to, one
            if 1 <= response >= 200:
                return response

        # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)
            print()
