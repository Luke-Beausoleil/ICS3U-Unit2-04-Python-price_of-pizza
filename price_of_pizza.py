#!/usr/bin/env python3

# Created by: Luke Beausoleil
# Created on: April 2021
# This program calculates the price of pizza

import constants


def main():
    # this function calculates the cost of the pizza

    # input
    diameter = int(input("Enter the diameter of the pizza in inches: "))

    # process
    subtotal = (
        (constants.MATERIALS * diameter) + constants.LABOR + constants.RENT
    )
    price = subtotal * constants.HST

    # output
    print("")
    print("The price of a {} inch pizza is: ${:,.2f}".format(diameter, price))
    print("\nDone.")


if __name__ == "__main__":
    main()
