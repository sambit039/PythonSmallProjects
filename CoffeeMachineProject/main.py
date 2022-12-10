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
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resourse_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print("Sorry mate not enought {item}.")
            return False
    return True


is_on=True
while is_on:
    choice=input("what would you like?,(espresso/latte/cappuccino.-").lower()
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"Water:{resources['water']}ml")
        print(f"Milk:{resources['milk']}ml")
        print(f"Coffee:{resourses['coffee']}g")
        print(f"Money:${profit}")
    else:
        drink=MENU[choice]
        if is_resoures_sufficient(drink["ingredients"]):
            