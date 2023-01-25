import os

def clear():
    os.system('cls')

menu = [
    {
    "name" : "Espresso",
    "water" : 50,
    "coffee" : 18,
    "milk" : 0,
    "price" : 1.5,
    },
    {
    "name" : "Latte",
    "water" : 200,
    "coffee" : 24,
    "milk" : 150,
    "price" : 2.5,
    },
    {
    "name" : "Cappuccino",
    "water" : 250,
    "coffee" : 24,
    "milk" : 100,
    "price" : 3,
    },
]

machine_water = 300
machine_milk = 200
machine_coffee = 100
machine_money = 0

def report():
    print(f"Water: {machine_water}ml")
    print(f"Milk: {machine_milk}ml")
    print(f"Coffee: {machine_coffee}g")
    print(f"Money: ${machine_money}")

def dispense(coffee_type):
    available = check_ingredients(coffee_type)
    
    for i in range(0,len(menu)):
        if menu[i]["name"] == coffee_type:
            menu_item = i


    if available:
        cost = menu[i]["price"]
        money_inserted = 0
        quarters = 0
        dimes = 0
        nickels = 0
        pennies = 0

        while money_inserted < cost:
            print("Please insert Coins.")
            
            quarters += float(input("How many quarters?: "))  * .25
            dimes += float(input("How many dimes?: ")) * .1
            nickels += float(input("How many nickels?: ")) * .05
            pennies += float(input("How many pennies?: ")) * .01

            money_inserted = round(quarters + dimes + nickels + pennies,2)
            change = round(money_inserted - cost,2)
            
            if money_inserted < cost:
                print(f"You're short: {'{0:.2f}'.format(change * -1)}.  Money Refunded") 
                money_inserted = 0   
            
        
        print(f"Here is ${'{0:.2f}'.format(change)} in change.")
        print(f"Here is your {menu[menu_item]['name']}. Enjoy!")
        reduce_mats(coffee_type)
    

def check_ingredients(coffee_type):
    for i in range(0,len(menu)):
        if menu[i]["name"] == coffee_type:
            water_needed = menu[i]["water"]
            milk_needed = menu[i]["milk"]
            coffee_needed = menu[i]["coffee"]

            
            if water_needed > machine_water:
                print("Sorry not enough water.")
                return False
            elif coffee_needed > machine_coffee:
                print("sorry not enough coffee.")
                return False
            elif milk_needed > machine_milk:
                print("Sorry not enough milk.")
                return False
            else:
                return True
            
    

def reduce_mats(coffee_type):
    global machine_water, machine_coffee, machine_milk, machine_money
    for i in range(0,len(menu)):
        if menu[i]["name"] == coffee_type:
            machine_water -= menu[i]["water"]
            machine_milk -= menu[i]["milk"]
            machine_coffee -= menu[i]["coffee"]
            machine_money += menu[i]["price"]

            


electricity = True

while electricity:
    on_menu = False

    while not on_menu:
        coffee = input("What would you like? (espresso/latte/cappuccino): ").title()
        for i in range(0,len(menu)):
            if coffee == menu[i]["name"] or coffee == "Report" or coffee == "Off":
                on_menu = True
    
    if coffee == "Report":
        report()
    elif coffee == "Off":
        electricity = False
    else:
         dispense(coffee)

         print("hi")
    
    