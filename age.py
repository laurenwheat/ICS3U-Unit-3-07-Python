#!/usr/bin/env python3

# Created by: Lauren Wheatley
# Created on: May 2021
# This program uses a NOT boolean statement


def main():
    # this function uses a NOT boolean statement

    is_between_25_and_40_str = input("Enter your age: ")

    try:
        is_between_25_and_40 = int(is_between_25_and_40_str)

        if is_between_25_and_40 > 25 and is_between_25_and_40 < 40:
            print('Date my Grandchild!!!')
        else:
            print('You will never be my Grandchild in-law!')
    except Exception:
        print("That is not a valid input!")
    finally:
        print("Thanks for playing! <3")


if __name__ == "__main__":
    main()
