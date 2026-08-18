MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.8,
    }
}

ingredients = {
    "water": 300,
    "coffee": 100,
    "milk" : 200,
    "money" : 0
}

done = False

while not done == True:
        
    choice = input("What do you want? (latte/espresso/cappuccino): ").lower()

    if choice == "report":
        print(f"Water = {ingredients["water"]}ml\nCoffee = {ingredients["coffee"]}gm\nMilk = {ingredients["milk"]}ml\nMoney = {round(ingredients["money"], 2)}$")
        continue

    penny = int(input("How many pennies: ")) * 0.01 
    nickel = int(input("How many nickels: ")) * 0.05
    dime = int(input("How many dimes: ")) * 0.10
    quarter = int(input("How many quarters: ")) * 0.25

    total_paid = round(penny + nickel + dime + quarter , 2)
    print(f"Amount Paid = {total_paid}$")

    if choice == "cappuccino":
        if total_paid >= MENU["cappuccino"]["cost"]:
            if ingredients["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"] and ingredients["milk"] >= MENU["cappuccino"]["ingredients"]["milk"] and ingredients["water"] >= MENU["cappuccino"]["ingredients"]["water"]:
                ingredients["money"] += (total_paid - round((total_paid - MENU["cappuccino"]["cost"]), 2))
                ingredients["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                ingredients["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                ingredients["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
                print(f"Thank you for the money. Here is {round((total_paid - MENU["cappuccino"]["cost"]), 2)} as change")
            else:
                print("Sorry but there is not enough ingredients in the machine.")
                break
        else:
            print("Sorry you dont ahve the required funds")
            break

    elif choice == "latte":
        if total_paid >= MENU["latte"]["cost"]:
            if ingredients["coffee"] >= MENU["latte"]["ingredients"]["coffee"] and ingredients["milk"] >= MENU["latte"]["ingredients"]["milk"] and ingredients["water"] >= MENU["latte"]["ingredients"]["water"]:
                ingredients["money"] += (total_paid - round((total_paid - MENU["latte"]["cost"]), 2))
                ingredients["water"] -= MENU["latte"]["ingredients"]["water"]
                ingredients["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
                ingredients["milk"] -= MENU["latte"]["ingredients"]["milk"]
                print(f"Thank you for the money. Here is {round((total_paid - MENU["latte"]["cost"]), 2)} as change")
            else:
                print("Sorry but there is not enough ingredients in the machine.")
                break
        else:
            print("Sorry you dont ahve the required funds")
            break

    elif choice == "espresso":
        if total_paid >= MENU["espresso"]["cost"]:
            if ingredients["coffee"] >= MENU["espresso"]["ingredients"]["coffee"] and ingredients["milk"] >= MENU["espresso"]["ingredients"]["milk"] and ingredients["water"] >= MENU["espresso"]["ingredients"]["water"]:
                ingredients["money"] += (total_paid - round((total_paid - MENU["espresso"]["cost"]), 2))
                ingredients["water"] -= MENU["espresso"]["ingredients"]["water"]
                ingredients["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
                ingredients["milk"] -= MENU["espresso"]["ingredients"]["milk"]
                print(f"Thank you for the money. Here is {round((total_paid - MENU["espresso"]["cost"]), 2)} as change")
            else:
                print("Sorry but there is not enough ingredients in the machine.")
                break

        else:
            print("Sorry you dont ahve the required funds")
            break

    question = input("Are you done (Y/N): ").lower()

    if question == "y":
        done = True

print("GOODBYE!")
