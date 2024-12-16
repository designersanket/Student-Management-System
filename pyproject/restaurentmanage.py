menu={
    'Pizza':80,
    'Burger':50,
    'Vada Pav':30,
    'cofee':60,
    'Veg Frankee':25,
    'choclate Shake':120
}

print("Wellcome To Sanket's Resturant.")
print("Pizza:80\n Burger:50\n Vada Pav:30\n Cofee:60\n Veg Frankee:25\n Choclate Shake:120\n")
print("What would you like to order.")

item_1=input("Please enter your order here:")

order_total=0

if item_1 in menu:
    order_total+=menu[item_1]
    print(f"Your order {item_1} has been placed successfully.")
else:
    print(f" item {item_1} is not available yet.")
    print("Chose another item.")

user_choise=input("Do you want to add another item?(Yess/No)!:")
if user_choise=="Yes":
    item_2=input("Enter your second order here:")
    if item_2 in menu:
        order_total+=menu[item_2]
        print(f"Your order {item_2} has been placed successfully.")
    else:
        print(f"Item {item_2} is not Present yet.")


print(f"The total amount of item is : {order_total}")
