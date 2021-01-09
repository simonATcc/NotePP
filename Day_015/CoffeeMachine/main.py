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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money_unit={
    "quarter":0.25,
    "dime":0.1,
    "nickle":0.05,
    "pennie":0.01,
}

OFF="off"
REPORT="report"

machine_money={
    "quarter":100,
    "dime":100,
    "nickle":100,
    "pennie":100,    
}
customer_money={
    "quarter":0,
    "dime":0,
    "nickle":0,
    "pennie":0,    
}

def money_total(mon):
    sum=0
    for key in mon:
        sum+=mon[key]*money_unit[key]
    return sum

def print_resources():
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} ml")
    print(f"Money: $ {money_total(machine_money)}")            

def is_sufficient(coffee_type):
    ingredients=MENU[coffee_type]["ingredients"]
    lake_item=[]
    for itemkey in ingredients:
        if resources[itemkey] < ingredients[itemkey]:
            lake_item.append(itemkey)
    return lake_item

def income(money1,money2,cost):
    amount=cost
    earn={}
    for item in money2:
        quantity=int(amount/money2[item])
        earn[item]=quantity
        amount-=quantity*money2[item]
    
    change={}
    for item in earn:
        money1[item]+=earn[item]
        change[item]=money2[item]-earn[item]

    return {"income":money1,"change":change}
def cook(res,ing):
    for item in ing:
        res[item]-=ing[item]
    return res

while True:
    coffee_type=input("What would you like? (espresso/latte/cappuccino):")

    if (coffee_type ==OFF):
        break

    if (coffee_type == REPORT):
        print_resources()
        continue
    
    lake_item=is_sufficient(coffee_type)
    if len(lake_item) > 0:
        print(f"Sorry there is not enough {','.join(lake_item)}.")
        continue

    for item in customer_money:
        customer_money[item]=int(input(f"insert {item}"))
    user_money_total=money_total(customer_money)
    coffee= MENU[coffee_type]
    coffee_cost=coffee["cost"]
    if user_money_total < coffee_cost:
        print("Sorry that's not enough money. Money refunded.")
        print(f"coffee_cost{coffee_cost}, your money {user_money_total}")    
        continue

    income_result=income(machine_money,customer_money,coffee_cost)

    machine_money=income_result["income"]
    user_change=income_result["change"]
    user_change_total=money_total(user_change)
    resources=cook(resources,coffee["ingredients"])
    if user_change_total >0 :
        print(f"Here is ${user_change_total:.2f} dollars in change.")
    
    print(f"Here is your {coffee_type}. Enjoy!”.")
    
    

    
    


    







