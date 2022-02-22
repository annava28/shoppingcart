# shopping_cart.py

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

#################### product input 
subtotal_price = 0
selected_ids = []

while True:
    selected_id = input("Please input a product identifier: ")
    if selected_id == "DONE" or selected_id == "done" or selected_id == "Done":
        break
    elif int(selected_id) > len(products) or int(selected_id) < 0: #I got this idea from a student during office hours on 2/21
        print("Oops! Please select a correct product indentifier")
    else:
        selected_ids.append(selected_id)
     
#################### receipt formatting
print("-----------------------------")
print("THE NOT-SO-HOYA SNAXA")
print("www.thenotsohoyasnaxa.com")
print("-----------------------------")

#################### displaying current date and time, https://www.programiz.com/python-programming/datetime/current-datetime
from datetime import datetime

now = datetime.now()
 
dt_string = now.strftime("%m/%d/%y %H:%M:%S")
print("CHECKOUT AT:", dt_string)
print("-----------------------------")
print("SELECTED PRODUCTS:")

#################### shopping cart items 

for selected_id in selected_ids:
    matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
    matching_product = matching_products[0]
    subtotal_price = subtotal_price + matching_product["price"]
    print("... ",matching_product["name"], "(" + str(to_usd(matching_product["price"])) + ")")


#################### subtotal, tax, total

import os 
from dotenv import load_dotenv

load_dotenv()


tax_rate = (os.getenv("TAX_RATE", default = 0.0875))

tax = subtotal_price * float(tax_rate)
total = subtotal_price + tax

#################### end of receipt
print("-----------------------------") 
print ("SUBTOTAL:", to_usd(subtotal_price))
print ("TAX:", to_usd(tax))
print ("TOTAL:", to_usd(total))
print("-----------------------------")
print("THANKS, SEE YOU AGAIN SOON!")
print("-----------------------------")

#################### e-mail
receipt = input("Would you like your receipt emailed to you? Yes / No ")

if receipt == "No" or receipt == "NO" or receipt == "no":
    print("Ok! Your receipt will not be emailed. Please refer to the above for your records.")
elif receipt == "Yes" or receipt == "YES" or receipt == "yes":

    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail

    load_dotenv()

    SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
    SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")

    client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
    print("CLIENT:", type(client))

    subject = "Your Receipt from The Not-So-Hoya Snaxa"

#source for how to reference a variable in HTML https://anvil.works/forum/t/how-to-add-a-python-variable-in-html-text-email/5323
    html_content = f"""
        <h1> Not-So-Hoya Snaxa Receipt </h1>
        <h3> Date: {dt_string}  <h/2> 
        <h3> Subtotal: {to_usd(subtotal_price)} <h/2>
        <h3> Tax: {to_usd(tax)} <h/3>
        <h2> Total: {to_usd(total)}
        <h3> Thank you for shopping at Not-So-Hoya Snaxa! Please come again soon! <h/3> 
        """

    print("HTML:", html_content)

    message = Mail(from_email=SENDER_ADDRESS, to_emails=SENDER_ADDRESS, subject=subject, html_content=html_content)

    try:
        response = client.send(message)

        print("RESPONSE:", type(response)) 
        print(response.status_code) 
        print(response.body)
        print(response.headers)

    except Exception as err:
        print(type(err))
        print(err)
else:
    "Oops! Please enter yes or no."


