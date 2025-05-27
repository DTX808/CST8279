'''
Author: <TARIK MADI >
Date: 2025-05-21
This program simulates a simple shopping cart.
By using a function, we can ask for  the user to restart as many times
without having to write the logic again and agains
Users can add items, specify quantities, and see the total cost.
The program uses exception handling to manage invalid inputs.
'''
print("Welcome to the shopping cart Program!")
def Shoping():
    while True:
        try:
            name = str(input("What is your name? "))
            price = float(input("What is the price? $"))
            quantity = int(input("How many items do you have? "))
            TotalCost = price * quantity
            if  TotalCost > 100:
                discount = TotalCost  * 0.10
                TotalCost *= 0.9
                print(f"\nYou saved ${discount:.2f} with a 10% discount!")
                print(f"Discounted Total: ${TotalCost:3}")
            print("Hi", name, "The total cost is $", TotalCost)
            break
        except ValueError:
            print("Invalid input, please try again")
while True:
    Shoping()
    restart = input("Would you like to shop again? (Yes/No) ")
    if restart.lower() != "yes":
        print("Thanks for shopping with us!")
        break






