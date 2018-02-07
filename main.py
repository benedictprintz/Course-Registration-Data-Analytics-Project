#!/usr/bin/python
#
#  The program was written by Benedict PRINTZ and Victor MAURER.
#

# random function
def randomfunction():
    return 0

# to display the bank interface
def main():
    # here, we need to implement for the flow
    # display the menu
    choice = "0"
    while (choice != "4"):
        print("")
        print("   Main Menu")
        print("=======================")
        print("1. Display Balance")
        print("2. Display Record")
        print("3. Update Address")
        print("4. Exit")
        print("")

        # allow the user to choose one of the functions in the menu
        choice = input("Please input your choice (1-4): ")

        print("")

        # check the input and call the correspondence function
        if (choice == "1"):
            callDisplayBalanceHandler()
        elif (choice == "2"):
            callDisplayRecordHandler()
        elif (choice == "3"):
            callUpdateAddressHandler()
        elif (choice == "4"):
            print("")
        else:
            print("Invalid Input!")


main()
