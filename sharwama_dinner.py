#!/usr/bin/env python3
# Created By: Jayden Smith
# Date: March 19, 2025
# This program calculates your shawarma dinner

import constants


def main():

    # Sets subtotal and user menu selections
    subtotal = 0

    main_course = input("Enter 1 for Shawarma Wrap or 0 for Shawarma Plate: ")
    side_course = input("Enter 1 for Meat Side or 0 for Vegetable Side: ")
    drink = input("Enter 1 for a Drink or 0 for No Drink: ")
    try:

        # Attempts to change the selections to integers
        main_course_int = int(main_course)
        side_course_int = int(side_course)
        drink_int = int(drink)

        match main_course_int:
            case 1:
                subtotal = constants.SHAWARMA_WRAP

                # Checks for all possible side and drink combos
                if side_course_int == 1:
                    subtotal = subtotal + constants.MEAT
                    if drink_int == 1:
                        subtotal = subtotal + constants.DRINK
                        tax = subtotal * constants.HST
                        total = subtotal + tax
                        print("Total cost is: ${:.2f}".format(total))
                    elif drink_int == 0:
                        tax = subtotal * constants.HST
                        total = subtotal + tax
                        print("Total cost is: ${:.2f}".format(total))

                    # If drink selection is invalid
                    else:
                        print("Please enter a valid drink option!")
                elif side_course_int == 0:
                    subtotal = subtotal + constants.VEGETABLE
                    if drink_int == 1:
                        subtotal = subtotal + constants.DRINK
                        tax = subtotal * constants.HST
                        total = subtotal + tax
                        print("Total cost is: ${:.2f}".format(total))
                    elif drink_int == 0:
                        tax = subtotal * constants.HST
                        total = subtotal + tax
                        print("Total cost is: ${:.2f}".format(total))

                    # If drink selection is invalid
                    else:
                        print("Please enter a valid drink option!")
                    # If side course is invalid
                else:
                    print("Please enter a valid side course option!")

            # If it is a plate
            case 0:
                subtotal = constants.SHAWARMA_PLATE
                if side_course_int == 1:
                    subtotal = subtotal + constants.MEAT
                    if drink_int == 1:
                        subtotal = subtotal + constants.DRINK
                        tax = subtotal * constants.HST
                        total = subtotal + tax
                        print("Total cost is: ${:.2f}".format(total))
                    elif drink_int == 0:
                        tax = subtotal * constants.HST
                        total = subtotal + tax
                        print("Total cost is: ${:.2f}".format(total))

                    # If drink selection is invalid
                    else:
                        print("Please enter a valid drink option!")
                elif side_course_int == 0:
                    subtotal = subtotal + constants.VEGETABLE
                    if drink_int == 1:
                        subtotal = subtotal + constants.DRINK
                        tax = subtotal * constants.HST
                        total = subtotal + tax
                        print("Total cost is: ${:.2f}".format(total))
                    elif drink_int == 0:
                        tax = subtotal * constants.HST
                        total = subtotal + tax
                        print("Total cost is: ${:.2f}".format(total))

                    # If drink selection is invalid
                    else:
                        print("Please enter a valid drink option!")
                    # If side course is invalid
                else:
                    print("Please enter a valid side course option!")

            # What happens if the main course is not one of the options
            case _:
                print("Invalid main course option. Please enter 0 or 1.")

    # What happens if the user selection is not a integer
    except ValueError:
        print("Please pick a valid menu option (enter 0 or 1)!")


if __name__ == "__main__":
    main()
