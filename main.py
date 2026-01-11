import re

from checkout import Checkout

"""
Entry point for the scanned items:
This file allows to interact with the implemented logic of checkout and pricing discounts
If any scanned item does not exists in the configuration then an exception arises resulting end of looping
"""

if __name__ =="__main__":
    #looping for getting scanned items 
    print(
        """Only enter the Scanned items SKUs like ABC.
         A, B and C being different items
         Do not add any non-alphabets""")

    while True:
        print("Enter 1 to entered new sequence, anything else to Exit")
        user_input = input()

        if user_input == "1":
            print("Enter new sequence: ")
            scanned_items = input()
            if re.match("^[a-zA-Z]+$", scanned_items):
                print(f"Scanned items are {scanned_items}")
                obj = Checkout()
                obj.scan_items(scanned_items)
                print(f"\nCheckout Total:{obj.checkout_total}")

            else:
                print("Enter only Alphabetic sequence")
        else:
            print("\n Exiting...")
            break
    