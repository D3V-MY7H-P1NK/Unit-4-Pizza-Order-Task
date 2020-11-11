import re

#Boolean Expressions
pizza_amount = False
pizza_size = False
top_select = False
deliver = False

#Arrays
customer_details = [] # Name, Address, Phone number
pizza_size_details = [] # Small, Medium, Large
topping_option = []

#Pizza Size and Costs
pizza_small = 3.25
pizza_medium = 5.50
pizza_large = 7.15

extra_topping = 0
delivery_charge = 2.50

#Pizza Topping Options
topping_1 = "Extra Cheese"
topping_2 = "Pepperoni"
topping_3 = "Bacon"
topping_4 = "Onion"
topping_5 = "Mushroom's"
topping_6 = "Olives"
topping_7 = "Ham"
topping_8 = "Pineapple"
topping_9 = "Prawn"
topping_10 = "Chilli"

address_regex = re.compile(r"[!]+[+]+\.[#]+")


print("\n|==================|", "\n|Pizza Order System|", "\n|==================|\n\n")

name = str(input("What is your name: "))
customer_details.append(name)

address = input("\nWhat is your address: ")
customer_details.append(address)
#if address_regex(address):
    #print("Good")

phone_num = input("\nWhat is your phone number: ")
customer_details.append(phone_num)
#if phone_regex.match(phone_num):
    #print("All good")

while pizza_amount == False:
    quantity = int(input("\nHow many pizzas do you want to order: "))
    if quantity >= 1 and quantity <= 6:
        print("You are ordering", quantity, "Pizza's.")
        pizza_amount = True
    elif quantity <= 0:
        print("\nYou cannot order negative Pizza's")
    elif quantity >= 7:
        print("\nYou cannot order more than 6 Pizza's")

print("\n|=====================|", "\n|Pizza Sizes and Costs|", "\n|=====================|")
print("\n1. Small =", pizza_small, "\n2. Medium =", pizza_medium, "\n3. Large =", pizza_large)


while pizza_size == False:
    pizza_remaining = quantity
    small_check = False
    medium_check = False
    large_check = False
    confirm_options = False

    small_size = 0
    medium_size = 0
    large_size = 0
    cost = 0
    pizza_cost = 0 

    if pizza_remaining > 1:

        #   SMALL PIZZA
        while small_check == False:
            small_size = int(input("\nHow many of your " + str(pizza_remaining) + " pizza's would you like small? "))

            if small_size == pizza_remaining or small_size <= pizza_remaining:
                print("\n", str(small_size), " pizza's are set to be small.")
                pizza_remaining = pizza_remaining - small_size
                cost = pizza_small * small_size
                pizza_cost = pizza_cost + cost
                small_check = True
                if pizza_remaining == 0:
                    pizza_size = True  
                    medium_check = True
                    large_check = True      
            elif small_size > pizza_remaining:
                print("\nYou did't order that many pizza's")

        #   MEDIUM PIZZA
        while medium_check == False:
            medium_size = int(input("\nHow many of your " + str(pizza_remaining) + " pizza's woulf you like medium? "))
            
            if medium_size == pizza_remaining or medium_size <= pizza_remaining:
                print("\n", str(medium_size), " pizza's are set to be medium.")
                pizza_remaining = pizza_remaining - medium_size
                cost = pizza_medium * pizza_size
                pizza_cost = pizza_cost + cost
                medium_check = True
                if pizza_remaining == 0:
                    pizza_size = True
                    large_check = True
            elif medium_size > pizza_remaining:
                print("\nYou did't order that many pizza's")

        #   LARGE PIZZA
        while large_check == False:
            large_size = int(input("\nHow many of your " + str(pizza_remaining) + " pizza's would you like large? "))

            if large_size == pizza_remaining or large_size <= pizza_remaining:
                print("\n", str(large_size), " pizza's are set to be large.")
                pizza_remaining = pizza_remaining - large_size
                cost = pizza_large * large_size
                pizza_cost = pizza_cost + cost
                large_check = True
                if pizza_remaining == 0:
                    pizza_size = True
                else:
                    pizza_size = False
                    confirm_options = True
                    print("\nYou haven't specified a size for all of the ordered Pizza's")
            elif large_size > pizza_remaining:
                print("\nYou did't order that many pizza's")
        
        # Store data in the list
        while confirm_options == False:
            pizza_size_details.append(small_size)
            pizza_size_details.append(medium_size)
            pizza_size_details.append(large_size)
            confirm_options = True


    elif quantity == 1:
        size = int(input("\nPlease enter the number for the size pizza you would like: "))
        if size == 1:
            small_size = small_size + 1
            pizza_size = True
        elif size == 2:
            medium_size = medium_size + 1
            pizza_size = True
        elif size == 3:
            large_size = large_size + 1
            pizza_size = True
        else:
            print("Invalid Input")
        
        pizza_size_details.append(small_size)
        pizza_size_details.append(medium_size)
        pizza_size_details.append(large_size)



print("\n|================|", "\n|Toppings Options|", "\n|================|")
print("\n1.", topping_1, "\n2.", topping_2, "\n3.", topping_3, "\n4.", topping_4, "\n5.", topping_5, "\n6.", topping_6, "\n7.", topping_7, "\n8.", topping_8, "\n9.", topping_9, "\n10.", topping_10)
toppings = input("\nWould you like to add toppings to your pizza? (Y/N) ")

while top_select == False:
    if toppings.lower() == "y":
        selection = int(input("\n\nPlease enter the number for the topping you would like to Add: "))
        if selection == 1:
            topping_option.append(topping_1)
        elif selection == 2:
            topping_option.append(topping_2)
        elif selection == 3:
            topping_option.append(topping_3)
        elif selection == 4:
            topping_option.append(topping_4)
        elif selection == 5:
            topping_option.append(topping_5)
        elif selection == 6:
            topping_option.append(topping_6)
        elif selection == 7:
            topping_option.append(topping_7)
        elif selection == 8:
            topping_option.append(topping_8)
        elif selection == 9:
            topping_option.append(topping_9)
        elif selection == 10:
            topping_option.append(topping_10)
        else:
            print("ERROR")

        more_toppings = input("\nWould you like to add more toppings? (Y/N) ")
        if more_toppings.lower() == "y":
            print("\n") # Restarts at begining of top_select While Statement
        elif more_toppings.lower() == "n":
            top_select = True
            amount_top = len(topping_option)

            if amount_top >= 4:
                extra_topping = 2.50
            elif amount_top == 3:
                extra_topping = 2
            elif amount_top == 2:
                extra_topping = 1.35
            elif amount_top == 1:
                extra_topping = 0.75

    elif toppings.lower() == "n":
        top_select = True
        extra_topping = 0
    
while deliver == False:
    delivery = 0

    delivery = input("\nDo you want delivery? (Y/N)")
    if delivery.lower == "y" or "n":
        deliver = True
    else:
        print("\nInvalid Input")

print("\n")

print("\n|=============|","\n|Order Summary|","\n|=============|")

print("\n|================|","\n|Customer Details|","\n|================|\n")
print("Name: ", customer_details[0])
print("Address: ", customer_details[1])
print("Phone Number: ", customer_details[2])

print("\n|=============|","\n|Pizza Details|","\n|=============|\n")
print("Small Pizza's Ordered: ", pizza_size_details[0])
print("Medium Pizza's Ordered: ", pizza_size_details[1])
print("Large Pizza's Ordered: ", pizza_size_details[2])
print("Ordered Toppings: ", topping_option)

print("\n|====|", "\n|Cost|", "\n|====|\n")
print("Pizza Cost = ", str(pizza_cost))
print("Topping Cost = ", str(extra_topping))
print("Delivery Cost = ", str(delivery_charge))

discount_check = pizza_cost + extra_topping

if discount_check > 20:
    discount = discount_check / 10
    total_cost = discount_check - discount

    dis = round(discount, 2)
    print("\nDiscount Applied = -", str(dis))
elif discount_check <= 20:
    total_cost = pizza_cost + extra_topping

if delivery.lower == "y":
    total_cost = total_cost + delivery_charge

tot = round(total_cost, 2)
print("\nTotal = ", str(tot))