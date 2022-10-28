MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# item_water = 0
# item_milk = 0
# item_coffee = 0

def report_resources():
    remaining_water = resources["water"]
    remaining_milk = resources["milk"]
    remaining_coffee = resources["coffee"]
    return (f"Water = {remaining_water}\n Milk = {remaining_milk}\n Coffee = {remaining_coffee}")

def item_resources():
    item_water = MENU[user_choice]["ingredients"]["water"]
    item_milk = MENU[user_choice]["ingredients"]["milk"]
    item_coffee = MENU[user_choice]["ingredients"]["coffee"]
    return (f"Ingredients Required:  Water = {item_water}\n Milk = {item_milk}\n Coffee = {item_coffee}")
    #if remaining_water < item_water:
     #   print(f"Not enough water to make a {user_choice}")
      #  exit()
   # if remaining_coffee < item_coffee:
    #    print(f"Not enough coffee to make a {user_choice}")
     #   exit()
  #  if remaining_milk < item_milk:
   #     print(f"Not enough milk to make a {user_choice}")


# def print_cost():

#Prompt user 'What would you like? (espresso/latte/cappaccino:'
user_choice = input("What would you like? (espresso/latte/cappaccino): ")

# print resource report
if user_choice == "report":
    print(report_resources())

# off will end execution
elif user_choice == "off":
    exit()

else:
    print()


#Check item cost
item_cost = MENU[user_choice]["cost"]
print(f"{user_choice} costs {item_cost}")

#Get users payment and store in "total_paid" variable
quarters = input("How many quarters would you like to add: ")
dimes = input("How many dimes would you like to add: ")
nickles = input("How many nickles would you like to add: ")
pennies = input("How many pennies would you like to add: ")
total_paid = float(quarters) * .25 + float(dimes) * .10 + float(nickles) * .05 + float(pennies) * .01

#TODO Check resources when user chooses a drink
item_resources()



#TODO Process Coins....

#TODO Subtract resources from inventory


#TODO Provide Item to customer
print(f"Here is your {user_choice}")

#TODO Provide Change to customer
change = round(total_paid - item_cost, 2)
print(f"{change} is your change")

